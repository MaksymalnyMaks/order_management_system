import requests


if __name__ == '__main__':
    # URL of the endpoint that exports orders from XML format
    url = 'http://127.0.0.1:5000/import_orders_from_xml'

    # XML STRUCTURE MUST BE THE SAME AS EXAMPLE, ALL TAGS MUST HAVE SPECIFIC NAME (THE SAME AS IN EXAMPLE)!
    # xml example available here: api_examples/xml_example.xml

    # Path to the XML file to be uploaded
    file_path = r'C:\Users\MaksymalnyMaks\python\order_management_system\orders_1719263191.xml'  # SPECIFY YOUR PATH INSIDE r''

    # Send POST request to import orders
    with open(file_path, 'rb') as file:
        files = {'xml_file': file}
        response = requests.post(url, files=files)

    if response.status_code == 200:
        response_content = response.json()
        print('Message:', response_content['message'])
        print('Invalid orders:')
        if 'invalid_orders' in response_content:
            print('Not imported orders:')
            for invalid_order in response_content['invalid_orders']:
                print(invalid_order)
    else:
        print('Failed to import orders. Status code:', response.status_code)
        response_content = response.json()
        print('Message:', response_content['message'])
        print('Invalid orders:')
        for invalid_order in response_content['invalid_orders']:
            print(invalid_order)
