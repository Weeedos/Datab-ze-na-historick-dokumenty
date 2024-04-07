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

            host = config["connection"]["host"].strip()
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
