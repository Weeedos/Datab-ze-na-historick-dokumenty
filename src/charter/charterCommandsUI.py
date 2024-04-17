import tkinter
from tkinter import filedialog, messagebox
from src.charter.charterSelectUI import CharterSelectUI
from src.charter.charter import Charter
from src.charter.charterDeleteUI import CharterDeleteUI
from src.charter.charterInsertUI import CharterInsertUI
from src.charter.charterUpdateUI import CharterUpdateUI
from src.log_editor.logeditor import LogEditor


class CharterCommandsUI:
    """
    Uživatelské rozhraní pro manipulaci s listinami.
    """
    def __init__(self, root, db_operator, admin):
        """
        Inicializuje uživatelské rozhraní pro manipulaci s listinami.
        """
        self.admin = admin
        self.log_editor = LogEditor()
        self.root = root
        self.db_operator = db_operator
        self.charter = Charter(self.db_operator)
        self.root.title("Listiny")

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
        Otevře okno pro vložení nové listiny.
        """
        charter_root_insert = tkinter.Tk()
        CharterInsertUI(charter_root_insert, self.charter)
        charter_root_insert.mainloop()

    def delete(self):
        """
        Otevře okno pro smazání existující listiny.
        """
        charter_root_delete = tkinter.Tk()
        CharterDeleteUI(charter_root_delete, self.charter)
        charter_root_delete.mainloop()

    def select(self):
        """
        Otevře okno pro vyhledání listin.
        """
        charter_root_select = tkinter.Tk()
        CharterSelectUI(charter_root_select, self.charter)
        charter_root_select.mainloop()

    def update(self):
        """
        Otevře okno pro aktualizaci existující listiny.
        """
        charter_root_update = tkinter.Tk()
        CharterUpdateUI(charter_root_update, self.charter)
        charter_root_update.mainloop()

    def import_csv(self):
        """
        Importuje data listin z CSV souboru do databáze.
        """
        try:
            path_to_csv = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            self.charter.import_from_csv(path_to_csv)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def export_csv(self):
        """
        Exportuje data listin z databáze do CSV souboru.
        """
        try:
            path_to_directory = tkinter.filedialog.askdirectory()
            if path_to_directory:
                self.charter.export_to_csv(path_to_directory)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def back(self):
        """
        Uzavírá aktuální okno.
        """
        self.root.destroy()
