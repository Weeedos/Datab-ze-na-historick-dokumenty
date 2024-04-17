import csv
import tkinter
import re
from tkinter import messagebox

from src.log_editor.logeditor import LogEditor


class Religion:
    """
    Třída Religion slouží k manipulaci s databází náboženských textů.
    """
    def __init__(self, db_operator):
        """
        Inicializuje novou instanci třídy Religion.
        """
        self.db_operator = db_operator
        self.log_editor = LogEditor()
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    def insert_into_religion(self, title, author, publication_date, description, language):
        """
        Vloží nový záznam o náboženském textu do databáze.
        """
        str_title = str(title)
        str_author = str(author)
        str_publication_date = str(publication_date)
        str_description = str(description)
        str_language = str(language)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"INSERT INTO religious_texts(title, author, publication_date, description, language) VALUES "
                            f"('{str_title}', '{str_author}', '{str_publication_date}', '{str_description}', '{str_language}')")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně přidán do databáze.")

    def delete_from_religion(self, title):
        """
        Odstraní záznam o náboženském textu z databáze.
        """
        str_title = str(title)
        self.cursor.execute(f"SELECT * FROM religious_texts WHERE title = '{str_title}'")
        output = self.cursor.fetchone()

        if output is None:
            messagebox.showerror("Chyba", "Listina s daným názvem nebyla nalezena.")

        self.cursor.execute(f"DELETE FROM religious_texts WHERE title = '{str_title}'")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně odebrán z databáze.")

    def update_religion(self, id, title, author, publication_date, description, language):
        """
        Aktualizuje existující záznam o náboženském textu v databázi.
        """
        int_id = int(id)
        str_title = str(title)
        str_author = str(author)
        str_publication_date = str(publication_date)
        str_description = str(description)
        str_language = str(language)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            raise Exception("Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"UPDATE religious_texts SET title = '{str_title}',"
                            f" publication_date = '{str_publication_date}', description = '{str_description}',"
                            f" author = '{str_author}', language = '{str_language}' WHERE id = {int_id}")
        self.connection.commit()

    def select_from_religion_by_title(self, title):
        """
        Vyhledá záznamy v databázi podle názvu náboženského textu.
        """
        str_title = str(title)
        self.cursor.execute(f"SELECT * FROM religious_texts WHERE title = '{str_title}'")
        return self.cursor.fetchall()

    def select_from_religion_by_author(self, author):
        """
        Vyhledá záznamy v databázi podle autora náboženského textu.
        """
        str_author = str(author)
        self.cursor.execute(f"SELECT * FROM religious_texts WHERE author = '{str_author}'")
        return self.cursor.fetchall()

    def select_from_religion_by_description(self, description):
        """
        Vyhledá záznamy v databázi podle popisu náboženského textu.
        """
        str_description = str(description)
        self.cursor.execute(f"SELECT * FROM religious_texts WHERE description = '{str_description}'")
        return self.cursor.fetchall()

    def select_from_religion_by_language(self, language):
        """
        Vyhledá záznamy v databázi podle jazyka náboženského textu.
        """
        str_language = str(language)
        self.cursor.execute(f"SELECT * FROM religious_texts WHERE language = '{str_language}'")
        return self.cursor.fetchall()

    def select_from_religion_by_publication_date(self, publication_date):
        """
        Vyhledá záznamy v databázi podle data vydání náboženského textu.
        """
        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")
        else:
            str_publication_date = str(publication_date)
            self.cursor.execute(f"SELECT * FROM religious_texts WHERE publication_date = '{str_publication_date}'")
            return self.cursor.fetchall()

    def select_from_religion_by_id(self, id):
        """
        Vyhledá záznamy v databázi podle ID náboženského textu.
        """
        int_id = int(id)
        self.cursor.execute(f"SELECT * FROM religious_texts WHERE id = '{int_id}'")
        return self.cursor.fetchall()

    def select_all(self):
        """
        Vrátí všechny záznamy z databáze.
        """
        self.cursor.execute("SELECT * FROM religious_texts")
        return self.cursor.fetchall()

    def import_from_csv(self, path_to_csv):
        """
        Importuje data z CSV souboru do databáze.
        """
        file = open(path_to_csv, "r", encoding="utf-8-sig")
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            self.insert_into_religion(row[0], row[1], row[2], row[3], row[4])

        file.close()

        self.log_editor.log_debug("Úspěšný import do databáze.")

    def export_to_csv(self, path_to_directory):
        """
        Exportuje data z databáze do CSV souboru.
        """
        data = self.select_all()

        with open(path_to_directory+"\export.csv", mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['nazev', 'autor', 'datum_vydani', 'popis', 'jazyk'])

            for row in data:
                writer.writerow(row[1:])

        self.log_editor.log_debug("Úspěšný export z databáze.")
