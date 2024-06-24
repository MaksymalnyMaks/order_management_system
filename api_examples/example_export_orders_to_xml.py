import requests
import time
import os
from pathlib import Path


if __name__ == '__main__':

    ROOT_DIRECTORY = str(Path().parent.absolute())

    # URL of the endpoint that exports orders in XML format
    url = "http://127.0.0.1:5000/export_orders_to_xml"

    # GET request to the endpoint in order to obtain data
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Define path of the directory where files are stored
        obtained_files_dir = os.path.join(ROOT_DIRECTORY, 'obtained_xml_files')

        # Create that directory if needed
        if not os.path.exists(obtained_files_dir):
            os.mkdir(obtained_files_dir)

        # Define XML file's path and save it
        file_path = os.path.join(obtained_files_dir, f'orders_{int(time.time())}.xml')
        with open(file_path, 'wb') as file:
            file.write(response.content)
    else:
        print("Failed to export orders. Status code:", response.status_code)
