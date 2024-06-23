import requests


if __name__ == '__main__':
    # URL of the endpoint that provides order statics
    url = "http://127.0.0.1:5000/order_statistics"

    # GET request to the endpoint in order to retrieve statistic about values from the orders table
    response = requests.get(url)
    if response.status_code == 200:
        obtained_data = response.json()
        # Presentation of the statistic
        print(f"The oldest records' IDs: {', '.join(obtained_data['oldest record IDs'])}")
        print(f"The latest records' IDs: {', '.join(obtained_data['newest record IDs'])}")
        print()
        print('The individual statues along with their occurrence frequencies:')
        for status, quantity in obtained_data['occurrence frequencies'].items():
            print(status + ':', quantity)
    else:
        print(f'Failed to obtain statics. Status code: {response.status_code}')

