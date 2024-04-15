import tkinter
from tkinter import filedialog, messagebox

from src.log_editor.log_editor import Log_editor
from src.religion.religion import Religion
from src.religion.religionDeleteUI import ReligionDeleteUI
from src.religion.religionInsertUI import ReligionInsertUI
from src.religion.religionSelectUI import ReligionSelectUI
from src.religion.religionUpdateUI import ReligionUpdateUI


class ReligionCommandsUI:
    def __init__(self, root, db_operator, admin):
        self.admin = admin
        self.log_editor = Log_editor()
        self.root = root
        self.db_operator = db_operator
        self.religion = Religion(self.db_operator)
        self.root.title("Náboženské texty")

        if self.admin == (0,):
            self.button_select = tkinter.Button(self.root, text="Vyhledat", command=self.select)
            self.button_select.grid(row=0, column=0, padx=10, pady=10)

            self.button_export_csv = tkinter.Button(self.root, text="Exportovat do CSV", command=self.export_csv)
            self.button_export_csv.grid(row=0, column=1, padx=10, pady=10)
        else:
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
        ReligionInsertUI(root_insert, self.religion)
        root_insert.mainloop()

    def delete(self):
        root_delete = tkinter.Tk()
        ReligionDeleteUI(root_delete, self.religion)
        root_delete.mainloop()

    def select(self):
        root_select = tkinter.Tk()
        ReligionSelectUI(root_select, self.religion)
        root_select.mainloop()

    def update(self):
        root_update = tkinter.Tk()
        ReligionUpdateUI(root_update, self.religion)
        root_update.mainloop()

    def import_csv(self):
        try:
            path_to_csv = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            self.religion.import_from_csv(path_to_csv)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def export_csv(self):
        try:
            path_to_directory = tkinter.filedialog.askdirectory()
            if path_to_directory:
                self.religion.export_to_csv(path_to_directory)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def back(self):
        self.root.destroy()
