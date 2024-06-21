from ordermanagment import app, api
from ordermanagment.resources.order import Order


if __name__ == '__main__':
    api.add_resource(Order, "/backend/<int:order_id>")
    app.run(debug=True)
