from flask_restful import Resource, reqparse, abort, fields, marshal_with
from sqlalchemy.exc import SQLAlchemyError
from ordermanagment.models import Orders
from datetime import datetime
from ordermanagment import db


class Order(Resource):
    # Parser for PUT requests: expects all fields to be provided
    order_put_args = reqparse.RequestParser()
    order_put_args.add_argument('order_name', type=str, help='Order_name is required!', required=True)
    order_put_args.add_argument('description', type=str, help='Description is required!', required=True)
    order_put_args.add_argument('creation_date', type=str, help='Creation_date is required!', required=True)
    order_put_args.add_argument('status', type=str, help='Status is required!', required=True)

    # Parser for PATCH requests: allows partial updates (fields are optional)
    order_update_args = reqparse.RequestParser()
    order_update_args.add_argument('order_name', type=str)
    order_update_args.add_argument('description', type=str)
    order_update_args.add_argument('creation_date', type=str)
    order_update_args.add_argument('status', type=str)

    # Defines how resource fields will be serialized in the response
    resource_fields = {
        'order_id': fields.Integer,        # Integer field for order ID
        'order_name': fields.String,       # String field for order name
        'description': fields.String,      # String field for description
        'creation_date': fields.DateTime,  # DateTime field for creation date
        'status': fields.String            # String field for status
    }

    @marshal_with(resource_fields)
    def get(self, order_id):
        # Query for the order by ID
        order = Orders.query.filter_by(order_id=order_id).first()
        if not order:
            abort(404, message="Record with given ID does not exist in the database!")
        return order

    @marshal_with(resource_fields)
    def put(self, order_id):
        args = self.order_put_args.parse_args()

        # Check if the order ID or order name already exists in the DB
        existing_order_id = Orders.query.filter_by(order_id=order_id).first()
        existing_order_name = Orders.query.filter_by(order_name=args['order_name']).first()

        if existing_order_id is not None:
            abort(409, message="Record with given ID exists in the database!")
        if existing_order_name is not None:
            abort(409, message="Record with given order name exists in the database!")

        # Parse the creation date
        try:
            creation_date = datetime.strptime(args['creation_date'], '%d.%m.%Y %H:%M:%S')
        except ValueError:
            abort(400, message="Invalid date format. Expected format is 'dd.mm.yyyy HH:MM:SS'")

        # Create a new order instance
        order = Orders(order_id=order_id, order_name=args['order_name'], description=args['description'],
                       creation_date=creation_date, status=args['status'])

        # Try to add the new order to DB
        try:
            db.session.add(order)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while adding the record: {str(e)}")

        return order, 201

    @marshal_with(resource_fields)
    def patch(self, order_id):
        args = self.order_update_args.parse_args()

        # Fetch the order by ID
        order = Orders.query.filter_by(order_id=order_id).first()

        # Check if in the database exists order with given ID
        if order is None:
            abort(404, message="Record with given id dose not exist in Database, cannot update!")

        # Check if the 'order_name' filed is supposed to be updated
        # Then check if new 'order_name' value is unique
        # And finally update value of the 'order_name' attribute
        if 'order_name' in args and args['order_name'] is not None:
            if Orders.query.filter_by(order_name=args['order_name']).first():
                abort(409, message="Record with given order_name exists in Database, cannot update!")
            order.order_name = args['order_name']

        # update values of attributes if their new value was passed in API request
        fields_to_update = ('description', 'creation_date', 'status')
        for field in fields_to_update:
            if field in args and args[field] is not None:
                setattr(order, field, args[field])

        # Try to update record in DB
        try:
            db.session.add(order)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while updating the record: {str(e)}")

        return order, 200

    def delete(self, order_id):
        # Fetch the order by ID
        order = Orders.query.filter_by(order_id=order_id).first()

        # Check if the order ID exists in the DB
        if order is None:
            abort(404, message="Record with given id dose not exist in Database!")

        # Try to delete record from DB
        try:
            db.session.delete(order)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while deleting the record: {str(e)}")

        return '', 204
