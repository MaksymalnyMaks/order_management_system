import requests


if __name__ == '__main__':
    # URL of the endpoint that handles CRUD operations for orders
    url = "http://127.0.0.1:5000/backend/"

    # ID of the record supposed to be read
    order_ID = '11'  # Replace this placeholder with valid ID

    # GEt request to the endpoint in order to retrieve specific order from the orders table in DB
    url_for_request = url + order_ID
    response = requests.get(url_for_request)

    if response.status_code == 200:
        print('The order successfully retrieved.')
        print(response.json())
    else:
        print(response.json())
        print('Failed to read order.')
