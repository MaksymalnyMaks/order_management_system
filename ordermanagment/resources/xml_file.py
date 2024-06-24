import xml.etree.ElementTree as ET
from flask import Response, request
from flask_restful import Resource, abort
from ordermanagment.models import Orders
from ordermanagment.enumerations.enums import Statuses
from ordermanagment import db
from datetime import datetime


class ExportOrders(Resource):

    def _generate_xml(self, orders: list):
        # Create the root element
        root = ET.Element("orders")

        # Add each order to the XML file
        for order in orders:
            order_element = ET.SubElement(root, "order")
            ET.SubElement(order_element, "orderID").text = str(order.order_id)
            ET.SubElement(order_element, "orderName").text = order.order_name
            ET.SubElement(order_element, "description").text = order.description
            ET.SubElement(order_element, "creationDate").text = order.creation_date.strftime("%d-%m-%Y %H:%M:%S")
            ET.SubElement(order_element, "status").text = order.status

        # Convert the XML tree to a string
        xml_string = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # Yield the XML string
        yield xml_string

    def get(self):
        # Retrieve all order from db
        orders = Orders.query.all()

        # Stream the XML response
        return Response(self._generate_xml(orders), mimetype='application/xml', headers={'Content-Disposition': 'attachment;filename=orders.xml'}, status=200)


class ImportOrders(Resource):

    def post(self):
        acceptable_statuses = (Statuses.NEW.value, Statuses.IN_PROGRESS.value, Statuses.COMPLETED.value)
        invalid_id_info = 'This id already exists in db'
        invalid_name_info = 'This name already exists in db'
        invalid_status_info = f'The status is not valid. Valid statuses: {acceptable_statuses}'
        invalid_orders = []
        any_order_added = False

        # Check if 'xml_file' was specified in files part of the request
        if 'xml_file' not in request.files:
            abort(400, message="No file delivered in the request")

        # Get the XML file from the request
        file = request.files['xml_file']

        # Check if some file was assigned to the 'xml_file' key
        if file.filename == '':
            abort(400, message="No file delivered in the request")

        # Check if the file has an XML extension
        if not file.filename.lower().endswith('.xml'):
            abort(400, message="No file delivered in the request")

        # Check if it is possible to read data from file
        try:
            # Parse the XML file
            tree = ET.parse(file)
            root = tree.getroot()
        except ET.ParseError:
            abort(400, message="Failed to parse XML file. Please ensure the file is valid XML.")

        # Initialize batch size and counter
        batch_size = 100
        batch = []

        # Iterate over each order in the XML and add to the batch
        for order_element in root.findall('order'):
            try:
                order_id = order_element.find('orderID').text
                order_name = order_element.find('orderName').text
                description = order_element.find('description').text
                creation_date = order_element.find('creationDate').text,
                status = order_element.find('status').text

                # Check if all required values was provided for each order
                if not (order_id and order_name and description and creation_date and status):
                    raise ValueError("All fields (orderID, orderName, description, creationDate, status) are required")

                order_id = int(order_id)
                creation_date = datetime.strptime(creation_date[0], '%d.%m.%Y %H:%M:%S')

                # Validate provided values
                existing_order_id = Orders.query.filter_by(order_id=order_id).first()
                existing_order_name = Orders.query.filter_by(order_name=order_name).first()
                valid_status = status in acceptable_statuses

                reasons = []
                if existing_order_id:
                    reasons.append(invalid_id_info)
                if existing_order_name:
                    reasons.append(invalid_name_info)
                if not valid_status:
                    reasons.append(invalid_status_info)

                if reasons:
                    invalid_orders.append({'id': order_id, 'reasons': reasons})
                else:
                    # Create a new order object
                    order = Orders(order_id=order_id, order_name=order_name, description=description,
                                   creation_date=creation_date, status=status)
                    batch.append(order)
                    any_order_added = True

                    # Commit batch if batch size is reached
                    if len(batch) >= batch_size:
                        try:
                            db.session.bulk_save_objects(batch)
                            db.session.commit()
                        except Exception as e:
                            db.session.rollback()
                            return {"message": "Error saving batch to database"}, 500
                        batch.clear()

            except (AttributeError, ValueError) as e:
                abort(400, message=f"Error processing order data: {str(e)}")

        if batch:
            try:
                db.session.bulk_save_objects(batch)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return {"message": "Error saving final batch to database"}, 500

        if not invalid_orders:
            return {"message": "All orders successfully imported from XML"}, 200
        elif any_order_added:
            return {"message": "Some orders couldn't be imported from XML (invalid values)",
                    "invalid_orders": invalid_orders}, 200
        else:
            return {"message": "No orders successfully imported from XML (invalid values)",
                    "invalid_orders": invalid_orders}, 400
