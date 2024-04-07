import mysql.connector
import configparser
import re


class DatabaseOperator:
    """
        A class for handling interactions with a MySQL database, including connecting, inserting, updating, and querying data.
    """
    def __init__(self):
        """
            Initialize the DatabaseOperator class with default values for connection attributes.
        """
        self.connection = None
        self.cursor = None

    def connect(self):
        """
            Establish a connection to the MySQL database using the configuration specified in the 'config.ini' file.
        """
        if self.connection is None:
            config = configparser.ConfigParser()
            config.read("./cfg/config.ini")

            required_keys = ["host", "user", "password", "database"]
            for key in required_keys:
                if key not in config["connection"] or not config["connection"][key].strip():
                    raise ValueError(f"Invalid or missing '{key}' in the configuration.")

            host = config["connection"]["host"].strip()
            ipv4_pattern = re.compile(
                r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
            )
            if not ipv4_pattern.match(host):
                raise ValueError("Invalid IPv4 address in the 'host' parameter.")

            user = config['connection']['user'].strip()
            password = config['connection']['password'].strip()
            database = config['connection']['database'].strip()

            if not isinstance(user, str) or not isinstance(password, str) or not isinstance(database, str):
                raise ValueError("User, password, and database must be strings.")

            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            self.cursor = self.connection.cursor()

    def disconnect(self):
        """
            Close the database connection if it is open.
        """
        if self.connection is not None:
            self.connection.close()

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.cursor
