from ordermanagment import app, api
from ordermanagment.resources.order import Order
from ordermanagment.resources.report import Report
from ordermanagment.resources.data_analysis import DataAnalysis


if __name__ == '__main__':
    api.add_resource(Order, "/backend/<int:order_id>")
    api.add_resource(Report, "/generate_report")
    api.add_resource(DataAnalysis, '/order_statistics')
    app.run(debug=True)
