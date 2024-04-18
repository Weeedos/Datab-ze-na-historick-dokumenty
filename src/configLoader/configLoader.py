import configparser
import os
import re


class ConfigLoader:
    def __init__(self):
        config_file = "./cfg/config.ini"
        if not os.path.isfile(config_file):
            raise FileNotFoundError("Konfigurační soubor nebyl nalezen.")

        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def getHost(self):
        host = self.config["connection"].get("host")
        if not host:
            raise ValueError("Hostitel není specifikován v konfiguračním souboru.")

        ipv4_with_port_regex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        if not re.match(ipv4_with_port_regex, host):
            raise ValueError("Neplatný formát hostitele. Měl by být ve formátu IPv4.")

        return host

    def getUser(self):
        user = self.config["connection"].get("user")
        if not user:
            raise ValueError("Uživatel není specifikován v konfiguračním souboru.")
        return user

    def getPassword(self):
        password = self.config["connection"].get("password")
        if not password:
            raise ValueError("Heslo není specifikováno v konfiguračním souboru.")
        return password

    def getDatabase(self):
        database = self.config["connection"].get("database")
        if not database:
            raise ValueError("Databáze není specifikována v konfiguračním souboru.")
        return database
