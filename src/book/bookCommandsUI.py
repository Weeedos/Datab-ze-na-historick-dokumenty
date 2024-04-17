import tkinter
from tkinter import filedialog, messagebox

from src.book.book import Book
from src.book.bookDeleteUI import BookDeleteUI
from src.book.bookInsertUI import BookInsertUI
from src.book.bookSelectUI import BookSelectUI
from src.book.bookUpdateUI import BookUpdateUI
from src.charter.charterSelectUI import CharterSelectUI
from src.charter.charter import Charter
from src.charter.charterDeleteUI import CharterDeleteUI
from src.charter.charterInsertUI import CharterInsertUI
from src.log_editor.log_editor import Log_editor


class BookCommandsUI:
    def __init__(self, root, db_operator, admin):
        self.admin = admin
        self.log_editor = Log_editor()
        self.root = root
        self.db_operator = db_operator
        self.book = Book(self.db_operator)
        self.root.title("Knihy")

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
        book_root_insert = tkinter.Tk()
        BookInsertUI(book_root_insert, self.book)
        book_root_insert.mainloop()

    def delete(self):
        book_root_delete = tkinter.Tk()
        BookDeleteUI(book_root_delete, self.book)
        book_root_delete.mainloop()

    def select(self):
        book_root_select = tkinter.Tk()
        BookSelectUI(book_root_select, self.book)
        book_root_select.mainloop()

    def update(self):
        book_root_select = tkinter.Tk()
        BookUpdateUI(book_root_select, self.book)
        book_root_select.mainloop()

    def import_csv(self):
        try:
            path_to_csv = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            self.book.import_from_csv(path_to_csv)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def export_csv(self):
        try:
            path_to_directory = tkinter.filedialog.askdirectory()
            if path_to_directory:
                self.book.export_to_csv(path_to_directory)
        except Exception as err:
            messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
            self.log_editor.log_error(f"Chyba: {str(err)}")

    def back(self):
        self.root.destroy()
