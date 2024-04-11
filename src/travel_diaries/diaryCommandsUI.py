import tkinter
from tkinter import filedialog, messagebox
from src.log_editor.log_editor import Log_editor
from src.travel_diaries.diary import Diary
from src.travel_diaries.diaryDeleteUI import DiaryDeleteUI
from src.travel_diaries.diaryInsertUI import DiaryInsertUI
from src.travel_diaries.diarySelectUI import DiarySelectUI
from src.travel_diaries.diaryUpdateUI import DiaryUpdateUI


class DiaryCommandsUI:
    def __init__(self, root, db_operator):
        self.log_editor = Log_editor()
        self.root = root
        self.db_operator = db_operator
        self.diary = Diary(self.db_operator)
        self.root.title("Cestovní deníky")

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
        DiaryInsertUI(root_insert, self.diary)
        root_insert.mainloop()

    def delete(self):
        root_delete = tkinter.Tk()
        DiaryDeleteUI(root_delete, self.diary)
        root_delete.mainloop()

    def select(self):
        root_select = tkinter.Tk()
        DiarySelectUI(root_select, self.diary)
        root_select.mainloop()

    def update(self):
        root_select = tkinter.Tk()
        DiaryUpdateUI(root_select, self.diary)
        root_select.mainloop()

    def import_csv(self):
        try:
            path_to_csv = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            self.diary.import_from_csv(path_to_csv)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def export_csv(self):
        try:
            path_to_directory = tkinter.filedialog.askdirectory()
            if path_to_directory:
                self.diary.export_to_csv(path_to_directory)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def back(self):
        self.root.destroy()