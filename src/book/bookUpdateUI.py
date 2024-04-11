import tkinter
from tkinter import ttk, messagebox
from src.book.bookUpdateMenuUI import BookUpdateMenuUI


class BookUpdateUI:
    def __init__(self, root, book):
        self.root = root
        self.book = book
        self.root.title("Úprava")

        self.button_refresh = tkinter.Button(self.root, text="Obnovit", command=self.refresh)
        self.button_refresh.grid(row=0, column=0, padx=10, pady=5)

        self.label_id = tkinter.Label(self.root)
        self.label_id.grid(row=0, column=1, padx=10, pady=5)
        self.entry_id = tkinter.Entry(self.root)
        self.entry_id.grid(row=0, column=2, padx=10, pady=5)

        self.button_update = tkinter.Button(self.root, text="Upravit", command=self.update)
        self.button_update.grid(row=0, column=3, padx=10, pady=5)

        self.result_tree = ttk.Treeview(self.root, columns=("ID", "Název", "Autor", "Datum vydání", "Žánr", "Jazyk", "ISBN"),
                                        show="headings")
        self.result_tree.heading("ID", text="ID")
        self.result_tree.heading("Název", text="Název")
        self.result_tree.heading("Autor", text="Autor")
        self.result_tree.heading("Datum vydání", text="Datum vydání (RRRR-MM-DD)")
        self.result_tree.heading("Žánr", text="Žánr")
        self.result_tree.heading("Jazyk", text="Jazyk")
        self.result_tree.heading("ISBN", text="ISBN")
        self.result_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

        self.button_back = tkinter.Button(self.root, text="Zpět", command=self.back)
        self.button_back.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.refresh()

    def update(self):
        id = self.entry_id.get()
        select_id = self.book.select_from_book_by_id(id)

        if not select_id:
            messagebox.showerror("Chyba", "Záznam se zadaným ID neexitsuje.")
            raise Exception("Záznam se zadaným ID neexitsuje.")

        book_update_id_root = tkinter.Tk()
        BookUpdateMenuUI(book_update_id_root, self.book, id)
        book_update_id_root.mainloop()

    def refresh(self):
        self.result_tree.delete(*self.result_tree.get_children())

        for result in self.book.select_all():
            self.result_tree.insert("", "end", values=result)

    def back(self):
        self.root.destroy()
