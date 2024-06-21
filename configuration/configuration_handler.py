import os
import yaml
from cryptography.fernet import Fernet
from root_dir import ROOT_DIRECTORY


class ConfigurationHandler:
    secret_key_path = os.path.join(ROOT_DIRECTORY, 'configuration', 'secret_key.txt')
    config_file_path = os.path.join(ROOT_DIRECTORY, 'configuration', 'config.yml')

    def __init__(self, data_name: str):
        self.data_name = data_name

    def load_raw_data_value(self):
        with open(self.config_file_path, 'r') as data_file:
            read_data = yaml.safe_load(data_file)

        if read_data is None:
            ValueError('The config.yml is empty!')
        else:
            if self.data_name in read_data:
                return read_data[self.data_name]
            else:
                ValueError('The given data_name does exist in config.yml')

    def load_encrypted_data_value(self):
        try:
            with open(self.secret_key_path, 'r') as key_file:
                secret_key = key_file.read()
        except FileNotFoundError:
            FileNotFoundError('Generate your secrete file first, use method: generate_secret_key')

        with open(self.config_file_path, 'r') as data_file:
            read_data = yaml.safe_load(data_file)

        if read_data is None:
            ValueError('The config.yml is empty!')
        else:
            if self.data_name in read_data:
                return Fernet(secret_key).decrypt(read_data[self.data_name]).decode()
            else:
                ValueError('The given data_name does exist in config.yml')

    @classmethod
    def generate_secret_key(cls):
        secret_key = Fernet.generate_key().decode()
        with open(cls.secret_key_path, 'w') as key_file:
            key_file.write(secret_key)

    @classmethod
    def add_value(cls, key: str, value: str):
        with open(cls.config_file_path, 'r') as data_file:
            read_data = yaml.safe_load(data_file)
            if read_data is None:
                read_data = dict()
            read_data[key] = value

        with open(cls.config_file_path, 'w') as data_file:
            yaml.safe_dump(read_data, data_file)

    @classmethod
    def add_encrypted_value(cls, key: str, value: str):
        try:
            with open(cls.secret_key_path, 'r') as key_file:
                secret_key = key_file.read()
        except FileNotFoundError:
            FileNotFoundError('Generate your secrete file first, use method: generate_secret_key')

        with open(cls.config_file_path, 'r') as data_file:
            read_data = yaml.safe_load(data_file)
            if read_data is None:
                read_data = dict()
            read_data[key] = Fernet(secret_key).encrypt(value.encode()).decode()

        with open(cls.config_file_path, 'w') as data_file:
            yaml.safe_dump(read_data, data_file)


if __name__ == '__main__':
    # Generate secrete key. Use only one time, otherwise you won't be able to decode values from configuration/config.yml!
    # To generate secrete_key uncomment instruction below and execute this script
    # ConfigurationHandler.generate_secret_key()

    # Below instructions can rewrite some value in configuration/config.yml!'

    # To add new or rewrite value in configuration/config.yml uncomment instruction below and execute this script
    # IMPORTANT! Below instruction add raw value to configuration/config.yml
    # ConfigurationHandler.add_value('placeholder_for_name', 'placeholder_for_value')

    # To add new or rewrite value in configuration/config.yml uncomment instruction below and execute this script
    # IMPORTANT! Below instruction add encrypted value to configuration/config.yml
    # ConfigurationHandler.add_encrypted_value('placeholder_for_name', 'placeholder_for_value')

    pass
