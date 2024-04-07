import csv
import tkinter
import re
from tkinter import messagebox


class Charter:
    def __init__(self, db_operator):
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    def insert_into_charter(self, title, issuance_date, content, author, country, period):
        """
        Insert a new record into the 'charter' table based on user input for title, issuance date, content, author, country, and period.
        """
        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(issuance_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"INSERT INTO charter(title, issuance_date, content, author, country, period) VALUES "
                            f"('{title}', '{issuance_date}', '{content}', '{author}', '{country}', '{period}')")
        self.connection.commit()

    def delete_from_charter(self, charter_title):
        str_title = str(charter_title)
        self.cursor.execute(f"SELECT * FROM charter WHERE title = '{str_title}'")
        output = self.cursor.fetchone()

        if output is None:
            raise ValueError("Listina s daným názvem nebyla nalezena.")

        self.cursor.execute(f"DELETE FROM charter WHERE title = '{str_title}'")
        self.connection.commit()

    def select_from_charter_by_title(self, charter_title):
        str_title = str(charter_title)
        self.cursor.execute(f"SELECT * FROM charter WHERE title = '{str_title}'")
        return self.cursor.fetchall()

    def select_from_charter_by_author(self, charter_author):
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

    def select_all(self):
        self.cursor.execute("SELECT * FROM charter")
        return self.cursor.fetchall()

    def import_from_csv(self, path_to_csv):
        file = open(path_to_csv, "r", encoding="utf-8-sig")
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            print(row)
            self.insert_into_charter(row[0], row[1], row[2], row[3], row[4], row[5])

        file.close()

    def export_to_csv(self, path_to_directory):
        data = self.select_all()

        with open(path_to_directory, mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['Nazev', 'Datum vydani', 'Obsah', 'Autor', 'Zeme', 'Obdobi'])

            for row in data:
                writer.writerow(row[1:])
