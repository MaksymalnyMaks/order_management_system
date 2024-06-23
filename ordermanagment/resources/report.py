from flask_restful import Resource
from flask import send_file
from ordermanagment.models import Orders
from ordermanagment.report_generators.generate_xlsx_report import XlsxReportGenerator
from ordermanagment.enumerations.enums import Statuses
from io import BytesIO


class Report(Resource):
    # Definition of the columns' headers
    columns_headers = ["Order ID", "Order Name", "Description", "Creation Date", "Status"]

    # Definition of the status color mappings
    status_colors = {
        Statuses.NEW.value: '0099FF',
        Statuses.IN_PROGRESS.value: 'FFFF00',
        Statuses.COMPLETED.value: '00FF00'
    }

    def get(self):
        # Retrieve all order from db
        orders = Orders.query.all()

        # Create instance of XlsxReportGenerator, that implements report generation
        report_generator = XlsxReportGenerator(data=orders, columns_headers=self.columns_headers)
        workbook = report_generator.generate_orders_report(status_colors=self.status_colors)

        # Save the workbook to a bytes buffer
        output = BytesIO()
        workbook.save(output)
        output.seek(0)

        return send_file(output, as_attachment=True, download_name="orders_report.xlsx", mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
