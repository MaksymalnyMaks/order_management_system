import requests
from datetime import datetime


if __name__ == '__main__':
    # URL of the endpoint that handles CRUD operations for orders
    url = "http://127.0.0.1:5000/backend/"

    # Acceptable values of statuses
    acceptable_statuses = {
        1: 'New',
        2: 'In Progress',
        3: 'Completed'
    }

    # ID of the record supposed to be created
    order_ID = '4'  # Replace this placeholder with valid ID

    # Definition of fields and their values which are supposed to be updated.
    # The definition should include ONLY the fields that need to be updated!
    # The fields to be updated should be defined as shown in example_create_order.py
    new_order = {
        'status': acceptable_statuses[3],
    }

    # PATCH request to the endpoint in order to update order from the orders table in DB
    url_for_request = url + order_ID
    response = requests.patch(url_for_request, json=new_order, headers={'Content-Type': 'application/json'})

    if response.status_code == 200:
        print('The order successfully updated.')
    else:
        print(response.json())
        print('Failed to update order.')
