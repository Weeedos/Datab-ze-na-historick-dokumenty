import csv
import re
from tkinter import messagebox
from src.log_editor.logeditor import LogEditor


class Letter:
    """
    Třída Letter slouží k manipulaci s databází dopisů.
    """
    def __init__(self, db_operator):
        """
        Inicializuje novou instanci třídy Letter.
        """
        self.log_editor = LogEditor()
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    def insert_into_letter(self, sender, recipient, sending_date, content):
        """
        Vloží nový dopis do databáze.
        """
        str_sender = str(sender)
        str_recipient = str(recipient)
        str_sending_date = str(sending_date)
        str_content = str(content)

        date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not date_regex.match(sending_date):
            messagebox.showerror("Chyba", "Špatný formát data. Použijte formát RRRR-MM-DD.")

        self.cursor.execute(f"INSERT INTO letters(sender, recipient, sending_date, content) VALUES "
                            f"('{str_sender}', '{str_recipient}', '{str_sending_date}', '{str_content}')")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně přidán do databáze.")

    def delete_from_letter(self, sender, recipient):
        """
        Odstraní dopis z databáze.
        """
        str_sender = str(sender)
        str_recipient = str(recipient)
        self.cursor.execute(f"SELECT * FROM letters WHERE sender = '{str_sender}' AND recipient = '{str_recipient}'")
        output = self.cursor.fetchone()

        if output is None:
            messagebox.showerror("Chyba", "Dopis nebyl nalezen.")

        self.cursor.execute(f"DELETE FROM letters WHERE sender = '{str_sender}' AND recipient = '{str_recipient}'")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně odebrán z databáze.")

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
            self.insert_into_letter(row[0], row[1], row[2], row[3])

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

        with open(path_to_directory + "\export.csv", mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['odesilatel', 'prijemce', 'datum', 'obsah'])

            for row in data:
                writer.writerow(row[1:])

        messagebox.showinfo("Úspěch", "Úspěšný export z databáze.")
        self.log_editor.log_debug("Úspěšný export z databáze.")
