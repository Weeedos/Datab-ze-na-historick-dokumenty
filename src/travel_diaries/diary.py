import csv
import re
from tkinter import messagebox

from src.log_editor.logeditor import LogEditor


class Diary:
    """
    Třída Diary slouží k manipulaci s deníkovými záznamy uloženými v databázi.
    """
    def __init__(self, db_operator):
        """
        Inicializuje novou instanci třídy Diary.
        """
        self.log_editor = LogEditor()
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    def insert_into_diary(self, title, author, date, content):
        """
        Vkládá nový deníkový záznam do databáze.
        """
        str_title = str(title)
        str_author = str(author)
        str_date = date
        str_content = str(content)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"INSERT INTO travel_diaries(title, author, date, content) VALUES "
                            f"('{str_title}', '{str_author}', '{str_date}', '{str_content}')")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně přidán do databáze.")

    def delete_from_diary(self, title):
        """
        Odstraňuje deníkový záznam z databáze podle názvu.
        """
        str_title = str(title)
        self.cursor.execute(f"SELECT * FROM travel_diaries WHERE title = '{str_title}'")
        output = self.cursor.fetchone()

        if output is None:
            messagebox.showerror("Chyba", "Dopis nebyl nalezen.")

        self.cursor.execute(f"DELETE FROM travel_diaries WHERE title = '{str_title}'")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně odebrán z databáze.")

    def update_diary(self, id, title, author, date, content):
        """
        Aktualizuje existující deníkový záznam v databázi.
        """
        int_id = int(id)
        str_title = str(title)
        str_author = str(author)
        str_date = date
        str_content = str(content)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(date):
            raise Exception("Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"UPDATE travel_diaries SET title = '{str_title}',"
                            f" author = '{str_author}', date = '{str_date}',"
                            f" content = '{str_content}' WHERE id = {int_id}")
        self.connection.commit()

    def select_from_diary_by_title(self, title):
        """
        Vrací deníkové záznamy z databáze podle názvu.

        :return:
            Seznam deníkových záznamů odpovídajících zadanému názvu.
        """
        str_title = str(title)
        self.cursor.execute(f"SELECT * FROM travel_diaries WHERE title = '{str_title}'")
        return self.cursor.fetchall()

    def select_from_diary_by_author(self, author):
        """
        Vrací deníkové záznamy z databáze podle autora.

        :return:
            Seznam deníkových záznamů odpovídajících zadanému autorovi.
        """
        str_author = str(author)
        self.cursor.execute(f"SELECT * FROM travel_diaries WHERE author = '{str_author}'")
        return self.cursor.fetchall()

    def select_from_diary_by_content(self, content):
        """
        Vrací deníkové záznamy z databáze podle obsahu.

        :return:
            Seznam deníkových záznamů odpovídajících zadanému obsahu.
        """
        str_content = str(content)
        self.cursor.execute(f"SELECT * FROM travel_diaries WHERE content = '{str_content}'")
        return self.cursor.fetchall()

    def select_from_diary_by_date(self, date):
        """
        Vrací deníkové záznamy z databáze podle data.

        :return:
            Seznam deníkových záznamů odpovídajících zadanému datu.
        """
        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")
        else:
            str_date = str(date)
            self.cursor.execute(f"SELECT * FROM travel_diaries WHERE publication_date = '{str_date}'")
            return self.cursor.fetchall()

    def select_from_diary_by_id(self, id):
        """
        Vrací deníkový záznam z databáze podle ID.

        :return:
            Deníkový záznam odpovídající zadanému ID.
        """
        int_id = int(id)
        self.cursor.execute(f"SELECT * FROM travel_diaries WHERE id = '{int_id}'")
        return self.cursor.fetchall()

    def select_all(self):
        """
        Vrací všechny deníkové záznamy z databáze.

        :return:
            Seznam všech deníkových záznamů v databázi.
        """
        self.cursor.execute("SELECT * FROM travel_diaries")
        return self.cursor.fetchall()

    def import_from_csv(self, path_to_csv):
        """
        Importuje deníkové záznamy z CSV souboru do databáze.
        """
        if path_to_csv is None:
            messagebox.showerror("Chyba", "Nevybrali jste soubor.")

        file = open(path_to_csv, "r", encoding="utf-8-sig")
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            self.insert_into_diary(row[0], row[1], row[2], row[3])

        file.close()

        messagebox.showinfo("Úspěch", "Úspěšný import do databáze.")
        self.log_editor.log_debug("Úspěšný import do databáze.")

    def export_to_csv(self, path_to_directory):
        """
        Exportuje všechny deníkové záznamy z databáze do CSV souboru.
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
