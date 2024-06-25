# Order Management System

## Introduction

This repository contains the code for an Order Management System. The system offers the following features:

- **API Endpoints for CRUD Operations**: Handle Create, Read, Update, and Delete operations for orders in the database.
- **XLSX Report Generation**: Generate reports in XLSX format containing all orders, with rows color-coded by status:
  - **New**: Blue
  - **In Progress**: Yellow
  - **Completed**: Green
- **Statistics Generation**: Generate statistics about the orders, including the count of each status and details on the oldest and newest orders.
- **XML Import/Export**: Export all orders to an XML file and import new orders from an XML file.

## How to Run the Application

1. **Clone the Project**: Clone the repository to your local machine using the following command:
    ```sh
    git clone <repository_url>
    ```

2. **Install PostgreSQL**: Install and configure PostgreSQL.
   - For installation instructions, visit: [Install PostgreSQL](https://www.w3schools.com/postgresql/postgresql_install.php)
   - Consider using pgAdmin4 for GUI interaction with the database. More info: [pgAdmin4 Guide](https://www.w3schools.com/postgresql/postgresql_pgadmin4.php)

3. **Configure the Application**:
   - Configuration details are stored in `config.yml` inside the `configuration` directory.
   - To set up the configuration:
     - Navigate to `configuration/configuration_handler.py`.
     - Follow the comments in the file to work with the script.
     - **Generate your secret key. Do this only once!**
     - Set the required configuration using `ConfigurationHandler.add_value` or `ConfigurationHandler.add_encrypted_value`. Use `add_encrypted_value` for sensitive information like passwords.
     - The following keys need to be set along with their values:
       - `username`: PostgreSQL username
       - `password`: PostgreSQL password
       - `db_name`: Name of the database
       - `db_connection_info`: Database address (e.g., `localhost:5432`)

4. **Create or Import the Database**:
   - To create a new empty database:
     - Uncomment line 15 in `ordermanagement/__init__.py`.
     - Run `run.py`.
     - Stop the server by pressing `CTRL+C`.
     - Re-comment line 15.
   - To import an example database, use the file `example_db.sql`. For more information on importing, visit:
     - [Importing Database Guide](https://postgrespro.com/list/thread-id/2365052)
     - [Stack Overflow Guide](https://stackoverflow.com/questions/51566090/how-to-import-a-schema-sql-file-using-pgadmin-4)

5. **Install Dependencies**:
   - Execute the following command to install dependencies:
     ```sh
     pip install -r requirements.txt
     ```
   - Consider using `venv` or `pipenv` for virtual environment management.

6. **Start the Application**:
   - Run the application by executing the following command:
     ```sh
     python run.py
     ```

## API Examples

Each API endpoint has its own usage example in the `api_examples` directory. Each example file contains comments to guide you through using the file effectively.

- Example files that can be run without modifications:
  - `api_examples/example_xlsx_report.py`
  - `api_examples/example_data_analysis.py`
  - `api_examples/example_export_orders_to_xml.py`

- Modifications required for specific example files:
  - **Reading an Order**: `api_examples/example_read_order.py`
    - Replace the `order_ID` variable value with the ID of the order you want to retrieve.
  - **Updating an Order**: `api_examples/example_update_order.py`
    - Replace the `order_ID` variable value with the ID of the order you want to update.
    - Specify the fields to update in the `new_order` dictionary.
  - **Deleting an Order**: `api_examples/example_delete_order.py`
    - Replace the `order_ID` variable value with the ID of the order you want to delete from the orders table.
  - **Creating an Order**: `api_examples/example_create_order.py`
    - Replace the `order_ID` variable value with the ID of the order you want to add to the orders table.
    - Specify valid values for the fields in the `new_order` dictionary.
  - **Importing Orders from XML**: `api_examples/example_import_orders_from_xml.py`
    - Specify the path to the XML file containing the orders to be imported. Set this path as the value of the `file_path` variable.
    - The XML file can be generated using `generate_xml.py`.

After making the necessary adjustments to the API examples, you can run them by following these steps:

1. Open two command prompt windows in the root directory of the project.
2. In the first terminal, run the `run.py` file and leave it open. Remember to activate your virtual environment (`venv` or `pipenv`) if you are using one.
    ```sh
    python run.py
    ```
3. In the second terminal, run the desired example with the command `python <example_file>`, for instance:
    ```sh
    python api_examples/example_read_order.py
    ```

Following these steps will allow you to execute the example scripts and interact with the API endpoints.
