import tkinter
from tkinter import ttk


class LetterSelectUI:
    """
    Třída LetterSelectUI poskytuje uživatelské rozhraní pro vyhledávání dopisů v databázi.
    """
    def __init__(self, root, letter):
        """
        Inicializuje uživatelské rozhraní pro vyhledávání dopisů.
        """
        self.root = root
        self.letter = letter
        self.root.title("Vyhledávání")

        self.label_search = tkinter.Label(self.root, text="Hledat podle:")
        self.label_search.grid(row=0, column=0, padx=10, pady=5, sticky='we')

        self.search_options = ["Odesílatel", "Příjemce", "Datum odeslání", "Obsah"]
        self.search_var = tkinter.StringVar(self.root)
        self.search_var.set(self.search_options[0])
        self.search_dropdown = ttk.Combobox(self.root, textvariable=self.search_var, values=self.search_options)
        self.search_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.entry_search = tkinter.Entry(self.root)
        self.entry_search.grid(row=0, column=2, padx=10, pady=5, sticky='we')

        self.button_search = tkinter.Button(self.root, text="Hledat", command=self.search)
        self.button_search.grid(row=0, column=3, padx=10, pady=5, sticky='we')

        self.result_tree = ttk.Treeview(self.root, columns=("Odesílatel", "Příjemce", "Datum odeslání", "Obsah"),
                                        show="headings")
        self.result_tree.heading("Odesílatel", text="Odesílatel")
        self.result_tree.heading("Příjemce", text="Příjemce")
        self.result_tree.heading("Datum odeslání", text="Datum odeslání (RRRR-MM-DD)")
        self.result_tree.heading("Obsah", text="Obsah")
        self.result_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='we')

        self.button_back = tkinter.Button(self.root, text="Zpět", command=self.back)
        self.button_back.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def search(self):
        """
        Provede hledání dopisů podle zadaných kritérií.
        """
        search_by = self.search_var.get()
        search_term = self.entry_search.get()
        self.result_tree.delete(*self.result_tree.get_children())

        if search_by == "Odesílatel":
            results = self.letter.select_from_letter_by_sender(search_term)
        elif search_by == "Příjemce":
            results = self.letter.select_from_letter_by_recipient(search_term)
        elif search_by == "Datum odeslání":
            results = self.letter.select_from_letter_by_sending_date(search_term)
        elif search_by == "Obsah":
            results = self.letter.select_from_letter_by_content(search_term)

        for result in results:
            self.result_tree.insert("", "end", values=result[1:])

    def back(self):
        """
        Zavře okno.
        """
        self.root.destroy()
