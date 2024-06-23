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
    order_ID = '1'  # Replace this placeholder with valid ID

    # Definition of a new order
    new_order = {
        'order_name': f'Audi Q7 - order {order_ID}',  # The order name has to be unique
        'description': 'Client ordered the Q7 model in standard configuration. Color: silver.',
        'creation_date': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
        'status': acceptable_statuses[3]  # Chose a proper number from 'acceptable_statuses' and insert it in '[]'
    }

    # PUT request to the endpoint in order to add a new record to the orders table in DB
    url_for_request = url + order_ID
    response = requests.put(url_for_request, json=new_order, headers={'Content-Type': 'application/json'})

    if response.status_code == 201:
        print('The order successfully added.')
    else:
        print(response.json())
        print('Failed to add order.')
