import tkinter
from tkinter import filedialog, messagebox

from src.charter.charterSelectUI import CharterSelectUI
from src.charter.charter import Charter
from src.charter.charterDeleteUI import CharterDeleteUI
from src.charter.charterInsertUI import CharterInsertUI


class CharterCommandsUI:
    def __init__(self, root, db_operator):
        self.root = root
        self.db_operator = db_operator
        self.charter = Charter(self.db_operator)
        self.root.title("Listiny")

        self.button_insert = tkinter.Button(self.root, text="Vložit", command=self.insert)
        self.button_insert.grid(row=0, column=0, padx=10, pady=10)

        self.button_delete = tkinter.Button(self.root, text="Smazat", command=self.delete)
        self.button_delete.grid(row=0, column=1, padx=10, pady=10)

        self.button_select = tkinter.Button(self.root, text="Vyhledat", command=self.select)
        self.button_select.grid(row=0, column=2, padx=10, pady=10)

        self.button_import_csv = tkinter.Button(self.root, text="Importovat z CSV", command=self.import_csv)
        self.button_import_csv.grid(row=0, column=3, padx=10, pady=10)

        self.button_export_csv = tkinter.Button(self.root, text="Exportovat do CSV", command=self.export_csv)
        self.button_export_csv.grid(row=0, column=4, padx=10, pady=10)

        self.button_back = tkinter.Button(self.root, text="Zpátky", command=self.back)
        self.button_back.grid(row=1, column=2, padx=10, pady=10)

    def insert(self):
        charter_root_insert = tkinter.Tk()
        CharterInsertUI(charter_root_insert, Charter(self.db_operator))
        charter_root_insert.mainloop()

    def delete(self):
        charter_root_delete = tkinter.Tk()
        CharterDeleteUI(charter_root_delete, Charter(self.db_operator))
        charter_root_delete.mainloop()

    def select(self):
        charter_root_select = tkinter.Tk()
        CharterSelectUI(charter_root_select, Charter(self.db_operator))
        charter_root_select.mainloop()

    def import_csv(self):
        try:
            path_to_csv = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            self.charter.import_from_csv(path_to_csv)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")

    def export_csv(self):
        try:
            path_to_directory = tkinter.filedialog.askdirectory()
            if path_to_directory:
                self.charter.export_to_csv(path_to_directory)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")

    def back(self):
        self.root.destroy()
