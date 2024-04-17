import logging

class LogEditor:
    """
    Třída pro úpravu a záznam událostí do logovacího souboru.
    """
    def __init__(self):
        """
        Inicializační metoda třídy LogEditor pro nastavení logovacího souboru.
        """
        logging.basicConfig(filename="./log/app.log", filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
        logging.getLogger().setLevel(logging.DEBUG)

    def log_debug(self, message):
        """
        Zaznamenává událost s úrovní DEBUG do logovacího souboru.

        :param:
            message: Zpráva, která má být zaznamenána.
        """
        logging.debug(message)

    def log_error(self, message):
        """
        Zaznamenává událost s úrovní ERROR do logovacího souboru.

        :param:
            message: Zpráva, která má být zaznamenána.
        """
        logging.error(message)

    def log_info(self, message):
        """
        Zaznamenává událost s úrovní INFO do logovacího souboru.

        :param:
            message: Zpráva, která má být zaznamenána.
        """
        logging.info(message)
