import tkinter
from tkinter import filedialog, messagebox

from src.letter.letter import Letter
from src.letter.letterDeleteUI import LetterDeleteUI
from src.letter.letterInsertUI import LetterInsertUI
from src.letter.letterSelectUI import LetterSelectUI
from src.letter.letterUpdateUI import LetterUpdateUI
from src.log_editor.logeditor import LogEditor


class LetterCommandsUI:
    """
    Třída LetterCommandsUI poskytuje uživatelské rozhraní pro manipulaci s databází dopisů.
    """
    def __init__(self, root, db_operator, admin):
        """
        Inicializuje uživatelské rozhraní pro správu dopisů.
        """
        self.admin = admin
        self.log_editor = LogEditor()
        self.root = root
        self.db_operator = db_operator
        self.letter = Letter(self.db_operator)
        self.root.title("Dopisy")

        if self.admin == (0,):
            self.button_select = tkinter.Button(self.root, text="Vyhledat", command=self.select)
            self.button_select.grid(row=0, column=0, padx=10, pady=10, sticky='we')

            self.button_export_csv = tkinter.Button(self.root, text="Exportovat do CSV", command=self.export_csv)
            self.button_export_csv.grid(row=0, column=1, padx=10, pady=10, sticky='we')
        else:
            self.button_insert = tkinter.Button(self.root, text="Vložit", command=self.insert)
            self.button_insert.grid(row=0, column=0, padx=10, pady=10, sticky='we')

            self.button_delete = tkinter.Button(self.root, text="Smazat", command=self.delete)
            self.button_delete.grid(row=0, column=1, padx=10, pady=10, sticky='we')

            self.button_update = tkinter.Button(self.root, text="Upravit", command=self.update)
            self.button_update.grid(row=0, column=2, padx=10, pady=10, sticky='we')

            self.button_select = tkinter.Button(self.root, text="Vyhledat", command=self.select)
            self.button_select.grid(row=0, column=3, padx=10, pady=10, sticky='we')

            self.button_import_csv = tkinter.Button(self.root, text="Importovat z CSV", command=self.import_csv)
            self.button_import_csv.grid(row=0, column=4, padx=10, pady=10, sticky='we')

            self.button_export_csv = tkinter.Button(self.root, text="Exportovat do CSV", command=self.export_csv)
            self.button_export_csv.grid(row=0, column=5, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(self.root, text="Zpátky", command=self.back)
        self.button_back.grid(row=1, column=3, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def insert(self):
        """
        Otevře okno pro vložení nového dopisu.
        """
        root_insert = tkinter.Tk()
        LetterInsertUI(root_insert, self.letter)
        root_insert.mainloop()

    def delete(self):
        """
        Otevře okno pro smazání dopisu.
        """
        root_delete = tkinter.Tk()
        LetterDeleteUI(root_delete, self.letter)
        root_delete.mainloop()

    def select(self):
        """
        Otevře okno pro vyhledávání dopisů.
        """
        root_select = tkinter.Tk()
        LetterSelectUI(root_select, self.letter)
        root_select.mainloop()

    def update(self):
        """
        Otevře okno pro aktualizaci dopisu.
        """
        root_select = tkinter.Tk()
        LetterUpdateUI(root_select, self.letter)
        root_select.mainloop()

    def import_csv(self):
        """
        Importuje data z CSV souboru do databáze.
        """
        try:
            path_to_csv = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            self.letter.import_from_csv(path_to_csv)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def export_csv(self):
        """
        Exportuje data z databáze do CSV souboru.
        """
        try:
            path_to_directory = tkinter.filedialog.askdirectory()
            if path_to_directory:
                self.letter.export_to_csv(path_to_directory)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def back(self):
        """
        Zavře okno.
        """
        self.root.destroy()
