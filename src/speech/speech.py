import csv
import re
from tkinter import messagebox

from src.log_editor.logeditor import LogEditor


class Speech:
    """
    Třída Speech zajišťuje manipulaci s řečmi a manifesty.
    """

    def __init__(self, db_operator):
        """
        Inicializuje novou instanci třídy Speech.
        """
        self.log_editor = LogEditor()
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    # Metody pro manipulaci s databází

    def insert_into_speech(self, title, author, publication_date, content):
        """
        Vloží novou řeč nebo manifest do databáze.
        """
        str_title = str(title)
        str_author = str(author)
        str_publication_date = publication_date
        str_content = str(content)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"INSERT INTO speeches_and_manifestos(title, author, publication_date, content) VALUES "
                            f"('{str_title}', '{str_author}', '{str_publication_date}', '{str_content}')")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně přidán do databáze.")

    def delete_from_speech(self, title):
        """
        Odebere řeč nebo manifest z databáze podle názvu.
        """
        str_title = str(title)
        self.cursor.execute(f"SELECT * FROM speeches_and_manifestos WHERE title = '{str_title}'")
        output = self.cursor.fetchone()

        if output is None:
            messagebox.showerror("Chyba", "Dopis nebyl nalezen.")

        self.cursor.execute(f"DELETE FROM speeches_and_manifestos WHERE title = '{str_title}'")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně odebrán z databáze.")

    def update_speech(self, id, title, author, publication_date, content):
        """
        Aktualizuje řeč nebo manifest v databázi.
        """
        int_id = int(id)
        str_title = str(title)
        str_author = str(author)
        str_publication_date = str(publication_date)
        str_content = str(content)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            raise Exception("Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"UPDATE speeches_and_manifestos SET title = '{str_title}',"
                            f" author = '{str_author}', publication_date = '{str_publication_date}',"
                            f" content = '{str_content}' WHERE id = {int_id}")
        self.connection.commit()

    def select_from_speech_by_title(self, title):
        """
        Vrátí řeč nebo manifest z databáze podle názvu.

        :return:
            Tuple: Vrací řeč nebo manifest z databáze.
        """
        str_title = str(title)
        self.cursor.execute(f"SELECT * FROM speeches_and_manifestos WHERE title = '{str_title}'")
        return self.cursor.fetchall()

    def import_from_csv(self, path_to_csv):
        """
        Importuje data z CSV souboru do databáze.
        """
        if path_to_csv is None:
            messagebox.showerror("Chyba", "Nevybrali jste soubor.")

        file = open(path_to_csv, "r", encoding="utf-8-sig")
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            self.insert_into_speech(row[0], row[1], row[2], row[3])

        file.close()

        messagebox.showinfo("Úspěch", "Úspěšný import do databáze.")
        self.log_editor.log_debug("Úspěšný import do databáze.")

    def export_to_csv(self, path_to_directory):
        """
        Exportuje data z databáze do CSV souboru.
        """
        data = self.select_all()

        if path_to_directory is None:
            messagebox.showerror("Chyba", "Nevybrali jste cestu.")

        with open(path_to_directory+"\export.csv", mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['nazev', 'autor', 'datum', 'obsah'])

            for row in data:
                writer.writerow(row[1:])

        messagebox.showinfo("Úspěch", "Úspěšný export z databáze.")
        self.log_editor.log_debug("Úspěšný export z databáze.")
