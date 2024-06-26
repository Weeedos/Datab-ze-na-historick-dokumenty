import csv
import tkinter
import re
from tkinter import messagebox

from src.log_editor.logeditor import LogEditor


class Charter:
    """
    Třída pro manipulaci s daty listin v databázi.
    """
    def __init__(self, db_operator):
        """
        Inicializuje objekt pro manipulaci s daty listin v databázi.
        """
        self.log_editor = LogEditor()
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    def insert_into_charter(self, title, issuance_date, content, author, country, period):
        """
        Vloží nový záznam do tabulky 'charter' na základě uživatelského vstupu pro název, datum vydání, obsah, autora, zemi a období.
        """
        str_title = str(title)
        str_issuance_date = str(issuance_date)
        str_content = str(content)
        str_author = str(author)
        str_country = str(country)
        str_period = str(period)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(issuance_date):
            raise Exception("Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"INSERT INTO charter(title, issuance_date, content, author, country, period) VALUES "
                            f"('{str_title}', '{str_issuance_date}', '{str_content}', '{str_author}', '{str_country}', '{str_period}')")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně přidán do databáze.")

    def delete_from_charter(self, charter_title):
        """
        Odstraní záznam z tabulky 'charter' na základě názvu listiny.
        """
        str_title = str(charter_title)
        self.cursor.execute(f"SELECT * FROM charter WHERE title = '{str_title}'")
        output = self.cursor.fetchone()

        if output is None:
            raise ValueError("Listina s daným názvem nebyla nalezena.")

        self.cursor.execute(f"DELETE FROM charter WHERE title = '{str_title}'")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně odebrán z databáze.")

    def update_charter(self, id, title, issuance_date, content, author, country, period):
        """
        Aktualizuje záznam v tabulce 'charter' na základě ID.
        """
        int_id = int(id)
        str_title = str(title)
        str_issuance_date = str(issuance_date)
        str_content = str(content)
        str_author = str(author)
        str_country = str(country)
        str_period = str(period)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(issuance_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")
            raise Exception("Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"UPDATE charter SET title = '{str_title}', issuance_date = '{str_issuance_date}',"
                            f" content = '{str_content}', author = '{str_author}', country = '{str_country}',"
                            f" period = '{str_period}' WHERE id = {int_id}")
        self.connection.commit()

    def select_from_charter_by_title(self, charter_title):
        """
        Vyhledá záznam v tabulce 'charter' podle názvu listiny.

        :return:
            Výsledek vyhledávání.
        """
        str_title = str(charter_title)
        self.cursor.execute(f"SELECT * FROM charter WHERE title = '{str_title}'")
        return self.cursor.fetchall()

    def select_from_charter_by_author(self, charter_author):
        """
        Vyhledá záznamy v tabulce 'charter' podle autora.

        :return:
            Výsledek vyhledávání.
        """
        str_author = str(charter_author)
        self.cursor.execute(f"SELECT * FROM charter WHERE author = '{str_author}'")
        return self.cursor.fetchall()

    def select_from_charter_by_period(self, charter_period):
        str_period = str(charter_period)
        self.cursor.execute(f"SELECT * FROM charter WHERE period = '{str_period}'")
        return self.cursor.fetchall()

    def select_from_charter_by_country(self, charter_country):
        str_country = str(charter_country)
        self.cursor.execute(f"SELECT * FROM charter WHERE country = '{str_country}'")
        return self.cursor.fetchall()

    def select_from_charter_by_issuance_date(self, issuance_date):
        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(issuance_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")
        else:
            str_issuance_date = str(issuance_date)
            self.cursor.execute(f"SELECT * FROM charter WHERE issuance_date = '{str_issuance_date}'")
            return self.cursor.fetchall()

    def import_from_csv(self, path_to_csv):
        """
        Importuje data z CSV souboru do databáze.
        """
        file = open(path_to_csv, "r", encoding="utf-8-sig")
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            self.insert_into_charter(row[0], row[1], row[2], row[3], row[4], row[5])

        file.close()

        self.log_editor.log_debug("Úspěšný import do databáze.")

    def export_to_csv(self, path_to_directory):
        """
        Exportuje data z databáze do CSV souboru.
        """
        data = self.select_all()

        with open(path_to_directory + "\export.csv", mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['Nazev', 'Datum vydani', 'Obsah', 'Autor', 'Zeme', 'Obdobi'])

            for row in data:
                writer.writerow(row[1:])

        self.log_editor.log_debug("Úspěšný export z databáze.")

    def select_all(self):
        """
        Vybere všechny záznamy z tabulky 'charter'.

        :return:
        """
        self.cursor.execute("SELECT * FROM charter")
        return self.cursor.fetchall()
