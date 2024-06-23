import requests
import time
import os
from pathlib import Path


if __name__ == '__main__':

    ROOT_DIRECTORY = str(Path().parent.absolute())

    # URL of the endpoint that generates xlsx report
    url = "http://127.0.0.1:5000/generate_report"

    # GET request to the endpoint in order to obtain report
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Define path of the directory where reports are stored
        obtained_reports_dir = os.path.join(ROOT_DIRECTORY, 'obtained_reports')

        # Create that directory if needed
        if not os.path.exists(obtained_reports_dir):
            os.mkdir(obtained_reports_dir)

        # Define report path and save it
        report_path = os.path.join(obtained_reports_dir, f'orders_report_{int(time.time())}.xlsx')
        with open(report_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f'Failed to obtain report. Status code: {response.status_code}')
