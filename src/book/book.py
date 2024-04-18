import csv
import re
from tkinter import messagebox
from src.log_editor.logeditor import LogEditor


class Book:
    """
    Reprezentuje třídu pro správu operací souvisejících s knihami v databázi.
    """

    def __init__(self, db_operator):
        """
        Inicializuje objekt třídy Book.
        """
        self.log_editor = LogEditor()
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    def insert_into_book(self, title, author, publication_date, genre, language, isbn):
        """
        Vloží nový záznam knihy do databáze.
        """
        str_title = str(title)
        str_author = str(author)
        str_publication_date = str(publication_date)
        str_genre = str(genre)
        str_language = str(language)
        int_isbn = int(isbn)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"INSERT INTO book(title, author, publication_date, genre, language, isbn) VALUES "
                            f"('{str_title}', '{str_author}', '{str_publication_date}', '{str_genre}', '{str_language}', '{int_isbn}')")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně přidán do databáze.")

    def delete_from_book(self, book_title):
        """
        Smaže záznam knihy z databáze na základě názvu.
        """
        str_title = str(book_title)
        self.cursor.execute(f"SELECT * FROM book WHERE title = '{str_title}'")
        output = self.cursor.fetchone()

        if output is None:
            messagebox.showerror("Chyba", "Listina s daným názvem nebyla nalezena.")

        self.cursor.execute(f"DELETE FROM book WHERE title = '{str_title}'")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně odebrán z databáze.")

    def update_book(self, id, title, author, publication_date, genre, language, isbn):
        """
        Aktualizuje záznam knihy v databázi.
        """
        int_id = int(id)
        str_title = str(title)
        str_author = str(author)
        str_publication_date = str(publication_date)
        str_genre = str(genre)
        str_language = str(language)
        int_isbn = int(isbn)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            raise Exception("Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"UPDATE book SET title = '{str_title}', publication_date = '{str_publication_date}',"
                            f" genre = '{str_genre}', author = '{str_author}', language = '{str_language}',"
                            f" isbn = '{int_isbn}' WHERE id = {int_id}")
        self.connection.commit()

    def select_from_book_by_title(self, book_title):
        """
        Vybere záznamy knihy z databáze podle názvu.

        :return:
            list: Seznam záznamů knihy odpovídající zadanému názvu.
        """
        str_title = str(book_title)
        self.cursor.execute(f"SELECT * FROM book WHERE title = '{str_title}'")
        return self.cursor.fetchall()

    def select_from_book_by_author(self, book_author):
        """
        Vybere záznamy knihy z databáze podle autora.

        :return:
            list: Seznam záznamů knihy odpovídající zadanému autorovi.
        """
        str_author = str(book_author)
        self.cursor.execute(f"SELECT * FROM book WHERE author = '{str_author}'")
        return self.cursor.fetchall()

    def select_from_book_by_genre(self, book_genre):
        """
        Vybere záznamy knihy z databáze podle žánru.

        :return:
            list: Seznam záznamů knihy odpovídající zadanému žánru.
        """
        str_genre = str(book_genre)
        self.cursor.execute(f"SELECT * FROM book WHERE genre = '{str_genre}'")
        return self.cursor.fetchall()

    def select_from_book_by_language(self, book_language):
        """
        Vybere záznamy knihy z databáze podle jazyka.

        :return:
            list: Seznam záznamů knihy odpovídající zadanému jazyku.
        """
        str_language = str(book_language)
        self.cursor.execute(f"SELECT * FROM book WHERE language = '{str_language}'")
        return self.cursor.fetchall()

    def select_from_book_by_publication_date(self, publication_date):
        """
        Vybere záznamy knihy z databáze podle data publikace.

        :return:
            list: Seznam záznamů knihy odpovídající zadanému datu publikace.
        """
        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")
        else:
            str_publication_date = str(publication_date)
            self.cursor.execute(f"SELECT * FROM book WHERE publication_date = '{str_publication_date}'")
            return self.cursor.fetchall()

    def select_from_book_by_isbn(self, isbn):
        int_isbn = int(isbn)
        self.cursor.execute(f"SELECT * FROM book WHERE isbn = '{int_isbn}'")
        return self.cursor.fetchall()

    def select_from_book_by_id(self, id):
        """
        Vybere záznam knihy z databáze podle ID.

        :return:
            list: Seznam obsahující záznam knihy odpovídající zadanému ID.
        """
        int_id = int(id)
        self.cursor.execute(f"SELECT * FROM book WHERE id = '{int_id}'")
        return self.cursor.fetchall()

    def select_all(self):
        """
        Vybere všechny záznamy knihy z databáze.

        :return:
            list: Seznam obsahující všechny záznamy knihy z databáze.
        """
        self.cursor.execute("SELECT * FROM book")
        return self.cursor.fetchall()

    def import_from_csv(self, path_to_csv):
        """
        Importuje data knihy z CSV souboru do databáze.
        """
        file = open(path_to_csv, "r", encoding="utf-8-sig")
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            self.insert_into_book(row[0], row[1], row[2], row[3], row[4], row[5])

        file.close()

        self.log_editor.log_debug("Úspěšný import do databáze.")

    def export_to_csv(self, path_to_directory):
        """
        Exportuje data knihy z databáze do CSV souboru.
        """
        data = self.select_all()

        with open(path_to_directory+"\export.csv", mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['Nazev', 'Autor', 'Datum_vydani', 'Zanr', 'Jazyk', 'ISBN'])

            for row in data:
                writer.writerow(row[1:])

        self.log_editor.log_debug("Úspěšný export z databáze.")
