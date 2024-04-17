import mysql.connector
import configparser
import re

from src.log_editor.logeditor import LogEditor

class DatabaseOperator:
    """
    Třída pro manipulaci s MySQL databází, včetně navazování spojení, vkládání, aktualizaci a dotazy dat.
    """
    def __init__(self):
        """
        Inicializuje třídu DatabaseOperator s výchozími hodnotami atributů spojení.
        """
        self.log_editor = LogEditor()
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Naváže spojení s databází MySQL pomocí konfigurace specifikované v souboru 'config.ini'.
        """
        if self.connection is None:
            config = configparser.ConfigParser()
            config.read("./cfg/config.ini")

            host = config["connection"]["host"].strip()
            user = config["connection"]["user"].strip()
            password = config["connection"]["password"].strip()
            database = config["connection"]["database"].strip()

            if not isinstance(user, str) or not isinstance(password, str) or not isinstance(database, str):
                raise ValueError("Uživatel, heslo a název databáze musí být řetězce.")

            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            self.cursor = self.connection.cursor()

            self.log_editor.log_debug("Úspěšné připojení do databáze.")

    def disconnect(self):
        """
        Uzavře spojení s databází, pokud je otevřené.
        """
        if self.connection is not None:
            self.connection.close()

        self.log_editor.log_debug("Úspěšné odpojení do databáze.")

    def get_connection(self):
        """
        Vrátí objekt připojení k databázi.

        :return:
            connection: Připojení do databáze
        """
        return self.connection

    def get_cursor(self):
        """
        Vrátí databázový kurzor.

        :return:
            cursor: Databázový kurzor
        """
        return self.cursor
