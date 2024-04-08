import csv
import tkinter
import re
from tkinter import messagebox

from src.log_editor.log_editor import Log_editor


class Book:
    def __init__(self, db_operator):
        self.log_editor = Log_editor()
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    def insert_into_book(self, title, author, publication_date, genre, language, isbn):
        """
        Insert a new record into the 'charter' table based on user input for title, issuance date, content, author, country, and period.
        """
        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"INSERT INTO book(title, author, publication_date, genre, language, isbn) VALUES "
                            f"('{title}', '{author}', '{publication_date}', '{genre}', '{language}', '{isbn}')")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně přidán do databáze.")

    def delete_from_book(self, book_title):
        str_title = str(book_title)
        self.cursor.execute(f"SELECT * FROM book WHERE title = '{str_title}'")
        output = self.cursor.fetchone()

        if output is None:
            messagebox.showerror("Chyba", "Listina s daným názvem nebyla nalezena.")

        self.cursor.execute(f"DELETE FROM book WHERE title = '{str_title}'")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně odebrán z databáze.")

    def select_from_book_by_title(self, book_title):
        str_title = str(book_title)
        self.cursor.execute(f"SELECT * FROM book WHERE title = '{str_title}'")
        return self.cursor.fetchall()

    def select_from_book_by_author(self, book_author):
        str_author = str(book_author)
        self.cursor.execute(f"SELECT * FROM book WHERE author = '{str_author}'")
        return self.cursor.fetchall()

    def select_from_book_by_genre(self, book_genre):
        str_genre = str(book_genre)
        self.cursor.execute(f"SELECT * FROM book WHERE genre = '{str_genre}'")
        return self.cursor.fetchall()

    def select_from_book_by_language(self, book_language):
        str_language = str(book_language)
        self.cursor.execute(f"SELECT * FROM book WHERE language = '{str_language}'")
        return self.cursor.fetchall()

    def select_from_book_by_publication_date(self, publication_date):
        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")
        else:
            str_publication_date = str(publication_date)
            self.cursor.execute(f"SELECT * FROM book WHERE publication_date = '{str_publication_date}'")
            return self.cursor.fetchall()

    def select_all(self):
        self.cursor.execute("SELECT * FROM book")
        return self.cursor.fetchall()

    def import_from_csv(self, path_to_csv):
        file = open(path_to_csv, "r", encoding="utf-8-sig")
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            print(row)
            self.insert_into_book(row[0], row[1], row[2], row[3], row[4], row[5])

        file.close()

        self.log_editor.log_debug("Úspěšný import do databáze.")

    def export_to_csv(self, path_to_directory):
        data = self.select_all()

        with open(path_to_directory+"\export.csv", mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['Nazev', 'Autor', 'Datum_vydani', 'Zanr', 'Jazyk', 'ISBN'])

            for row in data:
                writer.writerow(row[1:])

        self.log_editor.log_debug("Úspěšný export z databáze.")
