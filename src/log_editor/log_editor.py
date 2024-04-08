import logging


class Log_editor:
    def __init__(self):
        logging.basicConfig(filename="./log/app.log", filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
        logging.getLogger().setLevel(logging.DEBUG)

    def log_debug(self, message):
        logging.debug(message)

    def log_error(self, message):
        logging.error(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_critical(self, message):
        logging.critical(message)

    def log_info(self, message):
        logging.info(message)
