import requests


if __name__ == '__main__':
    # URL of the endpoint that handles CRUD operations for orders
    url = "http://127.0.0.1:5000/backend/"

    # ID of the record supposed to be deleted
    order_ID = '1'  # Replace this placeholder with valid ID

    # DELETE request to the endpoint in order to delete specified report
    url_for_request = url + order_ID
    response = requests.delete(url_for_request)

    if response.status_code == 204:
        print('The order successfully deleted.')
    else:
        print(response.json())
        print('Failed to delete order.')
