import tkinter
from tkinter import filedialog, messagebox

from src.letter.letter import Letter
from src.letter.letterDeleteUI import LetterDeleteUI
from src.letter.letterInsertUI import LetterInsertUI
from src.letter.letterSelectUI import LetterSelectUI
from src.letter.letterUpdateUI import LetterUpdateUI
from src.log_editor.log_editor import Log_editor


class LetterCommandsUI:
    def __init__(self, root, db_operator):
        self.log_editor = Log_editor()
        self.root = root
        self.db_operator = db_operator
        self.letter = Letter(self.db_operator)
        self.root.title("Dopisy")

        self.button_insert = tkinter.Button(self.root, text="Vložit", command=self.insert)
        self.button_insert.grid(row=0, column=0, padx=10, pady=10)

        self.button_delete = tkinter.Button(self.root, text="Smazat", command=self.delete)
        self.button_delete.grid(row=0, column=1, padx=10, pady=10)

        self.button_update = tkinter.Button(self.root, text="Upravit", command=self.update)
        self.button_update.grid(row=0, column=2, padx=10, pady=10)

        self.button_select = tkinter.Button(self.root, text="Vyhledat", command=self.select)
        self.button_select.grid(row=0, column=3, padx=10, pady=10)

        self.button_import_csv = tkinter.Button(self.root, text="Importovat z CSV", command=self.import_csv)
        self.button_import_csv.grid(row=0, column=4, padx=10, pady=10)

        self.button_export_csv = tkinter.Button(self.root, text="Exportovat do CSV", command=self.export_csv)
        self.button_export_csv.grid(row=0, column=5, padx=10, pady=10)

        self.button_back = tkinter.Button(self.root, text="Zpátky", command=self.back)
        self.button_back.grid(row=1, column=3, padx=10, pady=10)

    def insert(self):
        root_insert = tkinter.Tk()
        LetterInsertUI(root_insert, self.letter)
        root_insert.mainloop()

    def delete(self):
        root_delete = tkinter.Tk()
        LetterDeleteUI(root_delete, self.letter)
        root_delete.mainloop()

    def select(self):
        root_select = tkinter.Tk()
        LetterSelectUI(root_select, self.letter)
        root_select.mainloop()

    def update(self):
        root_select = tkinter.Tk()
        LetterUpdateUI(root_select, self.letter)
        root_select.mainloop()

    def import_csv(self):
        try:
            path_to_csv = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            self.letter.import_from_csv(path_to_csv)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def export_csv(self):
        try:
            path_to_directory = tkinter.filedialog.askdirectory()
            if path_to_directory:
                self.letter.export_to_csv(path_to_directory)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def back(self):
        self.root.destroy()
