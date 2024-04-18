import csv
import re
from tkinter import messagebox
from src.log_editor.logeditor import LogEditor


class Chronicle:
    """
    Třída pro manipulaci s kronikami v databázi.
    """
    def __init__(self, db_operator):
        """
        Inicializuje objekt Chronicle.
        """
        self.log_editor = LogEditor()
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    def insert_into_chronicle(self, title, author, publication_date, genre, language):
        """
        Vloží záznam kroniky do databáze.
        """
        str_title = str(title)
        str_author = str(author)
        str_publication_date = str(publication_date)
        str_genre = str(genre)
        str_language = str(language)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"INSERT INTO chronicle(title, author, publication_date, genre, language) VALUES "
                            f"('{str_title}', '{str_author}', '{str_publication_date}', '{str_genre}', '{str_language}')")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně přidán do databáze.")

    def delete_from_chronicle(self, chronicle_title):
        """
        Odebere záznam kroniky z databáze.
        """
        str_title = str(chronicle_title)
        self.cursor.execute(f"SELECT * FROM chronicle WHERE title = '{str_title}'")
        output = self.cursor.fetchone()

        if output is None:
            messagebox.showerror("Chyba", "Kronika s daným názvem nebyla nalezena.")

        self.cursor.execute(f"DELETE FROM chronicle WHERE title = '{str_title}'")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně odebrán z databáze.")

    def update_chronicle(self, id, title, author, publication_date, genre, language):
        """
        Aktualizuje záznam kroniky v databáze.
        """
        int_id = int(id)
        str_title = str(title)
        str_author = str(author)
        str_publication_date = str(publication_date)
        str_genre = str(genre)
        str_language = str(language)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(publication_date):
            raise Exception("Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"UPDATE chronicle SET title = '{str_title}', publication_date = '{str_publication_date}',"
                            f" genre = '{str_genre}', author = '{str_author}', language = '{str_language}'"
                            f" WHERE id = {int_id}")
        self.connection.commit()

    def select_from_chronicle_by_title(self, chronicle_title):
        """
        Vrací záznamy kroniky podle názvu.

        :return:
            Seznam záznamů kroniky.
        """
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

    def select_from_chronicle_by_id(self, id):
        int_id = int(id)
        self.cursor.execute(f"SELECT * FROM chronicle WHERE id = '{int_id}'")
        return self.cursor.fetchall()

    def select_all(self):
        self.cursor.execute("SELECT * FROM chronicle")
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
            self.insert_into_chronicle(row[0], row[1], row[2], row[3], row[4])

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
            writer.writerow(['Nazev', 'Autor', 'Datum_vydani', 'Zanr', 'Jazyk'])

            for row in data:
                writer.writerow(row[1:])

        messagebox.showinfo("Úspěch", "Úspěšný export z databáze.")
        self.log_editor.log_debug("Úspěšný export z databáze.")
