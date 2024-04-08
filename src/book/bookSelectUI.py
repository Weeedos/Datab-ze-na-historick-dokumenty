import tkinter
from tkinter import ttk


class BookSelectUI:
    def __init__(self, root, book):
        self.root = root
        self.book = book
        self.root.title("Vyhledávání")

        self.label_search = tkinter.Label(self.root, text="Hledat podle:")
        self.label_search.grid(row=0, column=0, padx=10, pady=5, sticky=tkinter.W)

        self.search_options = ["Název", "Autor", "Datum vydání", "Žánr", "Jazyk", "ISBN"]
        self.search_var = tkinter.StringVar(self.root)
        self.search_var.set(self.search_options[0])
        self.search_dropdown = ttk.Combobox(self.root, textvariable=self.search_var, values=self.search_options)
        self.search_dropdown.grid(row=0, column=1, padx=10, pady=5)

        self.entry_search = tkinter.Entry(self.root)
        self.entry_search.grid(row=0, column=2, padx=10, pady=5)

        self.button_search = tkinter.Button(self.root, text="Hledat", command=self.search)
        self.button_search.grid(row=0, column=3, padx=10, pady=5)

        self.result_tree = ttk.Treeview(self.root, columns=("Název", "Autor", "Datum vydání", "Žánr", "Jazyk", "ISBN"),
                                        show="headings")
        self.result_tree.heading("Název", text="Název")
        self.result_tree.heading("Autor", text="Autor")
        self.result_tree.heading("Datum vydání", text="Datum vydání (RRRR-MM-DD)")
        self.result_tree.heading("Žánr", text="Žánr")
        self.result_tree.heading("Jazyk", text="Jazyk")
        self.result_tree.heading("ISBN", text="ISBN")
        self.result_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

        self.button_back = tkinter.Button(self.root, text="Zpět", command=self.back)
        self.button_back.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    def search(self):
        search_by = self.search_var.get()
        search_term = self.entry_search.get()
        self.result_tree.delete(*self.result_tree.get_children())

        if search_by == "Název":
            results = self.book.select_from_book_by_title(search_term)
        elif search_by == "Autor":
            results = self.book.select_from_book_by_author(search_term)
        elif search_by == "Období":
            results = self.book.select_from_book_by_genre(search_term)
        elif search_by == "Země":
            results = self.book.select_from_book_by_language(search_term)
        elif search_by == "Datum vydání":
            results = self.book.select_from_book_by_publication_date(search_term)
        elif search_by == "ISBN":
            results = self.book.select_from_book_by_isbn(search_term)

        for result in results:
            self.result_tree.insert("", "end", values=result)

    def back(self):
        self.root.destroy()
