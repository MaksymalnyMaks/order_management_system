from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from configuration.configuration_handler import ConfigurationHandler

# Read configuration data from configuration/config.yml
username = ConfigurationHandler('username').load_raw_data_value()
password = ConfigurationHandler('password').load_encrypted_data_value()
where_db = ConfigurationHandler('db_connection_info').load_raw_data_value()
db_name = ConfigurationHandler('db_name').load_raw_data_value()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{where_db}/{db_name}'
db = SQLAlchemy(app)
api = Api(app)

