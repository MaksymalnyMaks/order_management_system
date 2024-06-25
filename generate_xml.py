import os
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

if __name__ == '__main__':

    ROOT_DIRECTORY = str(Path().parent.absolute())

    acceptable_statuses = {
        1: 'New',
        2: 'In Progress',
        3: 'Completed'
    }

    orders = [
        {
            'order_id': '9',
            'order_name': f'Audi A4 - order 122',
            'description': 'Client ordered the A4 model in s-line configuration. Color: blue.',
            'creation_date': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
            'status': acceptable_statuses[1]
        },
        {
            'order_id': '10',
            'order_name': f'Audi A4 - order 10',
            'description': 'Client ordered the A4 model in s-line configuration. Color: yellow.',
            'creation_date': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
            'status': acceptable_statuses[1]
        },
        {
            'order_id': '122',
            'order_name': f'Audi R8 - order 11',
            'description': 'Client ordered the R8 model in standard configuration. Color: red.',
            'creation_date': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
            'status': acceptable_statuses[2]
        },
        {
            'order_id': '133',
            'order_name': f'Audi RS7 - order 133',
            'description': 'Client ordered the RS7 model in standard configuration. Color: black.',
            'creation_date': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
            'status': 'dupa'
        },
        {
            'order_id': '13',
            'order_name': f'Audi RS6 - order 13',
            'description': 'Client ordered the RS6 model in standard configuration. Color: green.',
            'creation_date': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
            'status': acceptable_statuses[1]
        }
    ]
    root = ET.Element("orders")

    for order in orders:
        order_element = ET.SubElement(root, "order")
        ET.SubElement(order_element, "orderID").text = order['order_id']
        ET.SubElement(order_element, "orderName").text = order['order_name']
        ET.SubElement(order_element, "description").text = order['description']
        ET.SubElement(order_element, "creationDate").text = order['creation_date']
        ET.SubElement(order_element, "status").text = order['status']

    xml_string = ET.tostring(root, encoding='utf-8', xml_declaration=True)

    file_path = os.path.join(ROOT_DIRECTORY, f'orders_{int(time.time())}.xml')
    with open(file_path, 'wb') as file:
        file.write(xml_string)
