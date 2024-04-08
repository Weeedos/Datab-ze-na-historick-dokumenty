import csv
import tkinter
import re
from tkinter import messagebox

from src.log_editor.log_editor import Log_editor


class Chronicle:
    def __init__(self, db_operator):
        self.log_editor = Log_editor()
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    def insert_into_chronicle(self, title, author, publication_date, genre, language):
        """
        Insert a new record into the 'charter' table based on user input for title, issuance date, content, author, country, and period.
        """
        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"INSERT INTO chronicle(title, author, publication_date, genre, language) VALUES "
                            f"('{title}', '{author}', '{publication_date}', '{genre}', '{language}')")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně přidán do databáze.")

    def delete_from_chronicle(self, chronicle_title):
        str_title = str(chronicle_title)
        self.cursor.execute(f"SELECT * FROM chronicle WHERE title = '{str_title}'")
        output = self.cursor.fetchone()

        if output is None:
            messagebox.showerror("Chyba", "Listina s daným názvem nebyla nalezena.")

        self.cursor.execute(f"DELETE FROM chronicle WHERE title = '{str_title}'")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně odebrán z databáze.")

    def select_from_chronicle_by_title(self, chronicle_title):
        str_title = str(chronicle_title)
        self.cursor.execute(f"SELECT * FROM chronicle WHERE title = '{str_title}'")
        return self.cursor.fetchall()

    def select_from_chronicle_by_author(self, chronicle_author):
        str_author = str(chronicle_author)
        self.cursor.execute(f"SELECT * FROM chronicle WHERE author = '{str_author}'")
        return self.cursor.fetchall()

    def select_from_chronicle_by_genre(self, chronicle_genre):
        str_genre = str(chronicle_genre)
        self.cursor.execute(f"SELECT * FROM chronicle WHERE genre = '{str_genre}'")
        return self.cursor.fetchall()

    def select_from_chronicle_by_language(self, chronicle_language):
        str_language = str(chronicle_language)
        self.cursor.execute(f"SELECT * FROM chronicle WHERE language = '{str_language}'")
        return self.cursor.fetchall()

    def select_from_chronicle_by_publication_date(self, publication_date):
        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")
        else:
            str_publication_date = str(publication_date)
            self.cursor.execute(f"SELECT * FROM chronicle WHERE publication_date = '{str_publication_date}'")
            return self.cursor.fetchall()

    def select_all(self):
        self.cursor.execute("SELECT * FROM chronicle")
        return self.cursor.fetchall()

    def import_from_csv(self, path_to_csv):
        if path_to_csv is None:
            messagebox.showerror("Chyba", "Nevybrali jste soubor.")

        file = open(path_to_csv, "r", encoding="utf-8-sig")
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            print(row)
            self.insert_into_chronicle(row[0], row[1], row[2], row[3], row[4])

        file.close()

        messagebox.showinfo("Úspěch", "Úspěšný import do databáze.")
        self.log_editor.log_debug("Úspěšný import do databáze.")

    def export_to_csv(self, path_to_directory):
        data = self.select_all()

        if path_to_directory is None:
            messagebox.showerror("Chyba", "Nevybrali jste cestu.")

        with open(path_to_directory+"\export.csv", mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['Nazev', 'Autor', 'Datum_vydani', 'Zanr', 'Jazyk'])

            for row in data:
                writer.writerow(row[1:])

        messagebox.showinfo("Úspěch", "Úspěšný export z databáze.")
        self.log_editor.log_debug("Úspěšný export z databáze.")
