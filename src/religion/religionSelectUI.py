import tkinter
from tkinter import ttk


class ReligionSelectUI:
    """
    Třída ReligionSelectUI poskytuje uživatelské rozhraní pro vyhledávání náboženských textů v databázi.
    """

    def __init__(self, root, religion):
        """
        Inicializuje novou instanci třídy ReligionSelectUI.
        """
        self.root = root
        self.religion = religion
        self.root.title("Vyhledávání")

        self.label_search = tkinter.Label(self.root, text="Hledat podle:")
        self.label_search.grid(row=0, column=0, padx=10, pady=5, sticky='we')

        self.search_options = ["Název", "Autor", "Datum vydání", "Popis", "Jazyk"]
        self.search_var = tkinter.StringVar(self.root)
        self.search_var.set(self.search_options[0])
        self.search_dropdown = ttk.Combobox(self.root, textvariable=self.search_var, values=self.search_options)
        self.search_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.entry_search = tkinter.Entry(self.root)
        self.entry_search.grid(row=0, column=2, padx=10, pady=5, sticky='we')

        self.button_search = tkinter.Button(self.root, text="Hledat", command=self.search)
        self.button_search.grid(row=0, column=3, padx=10, pady=5, sticky='we')

        self.result_tree = ttk.Treeview(self.root, columns=("Název", "Autor", "Datum vydání", "Popis", "Jazyk"),
                                        show="headings")
        self.result_tree.heading("Název", text="Název")
        self.result_tree.heading("Autor", text="Autor")
        self.result_tree.heading("Datum vydání", text="Datum vydání (RRRR-MM-DD)")
        self.result_tree.heading("Popis", text="Popis")
        self.result_tree.heading("Jazyk", text="Jazyk")
        self.result_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='we')

        self.button_back = tkinter.Button(self.root, text="Zpět", command=self.back)
        self.button_back.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def search(self):
        """
        Provede vyhledávání na základě zadaného kritéria a zobrazí výsledky ve stromovém zobrazení.
        """
        search_by = self.search_var.get()
        search_term = self.entry_search.get()
        self.result_tree.delete(*self.result_tree.get_children())

        if search_by == "Název":
            results = self.religion.select_from_religion_by_title(search_term)
        elif search_by == "Autor":
            results = self.religion.select_from_religion_by_author(search_term)
        elif search_by == "Popis":
            results = self.religion.select_from_religion_by_description(search_term)
        elif search_by == "Jazyk":
            results = self.religion.select_from_religion_by_language(search_term)
        elif search_by == "Datum vydání":
            results = self.religion.select_from_religion_by_publication_date(search_term)

        if results is None:
            return

        for result in results:
            self.result_tree.insert("", "end", values=result[1:])

    def back(self):
        """
        Zavře aktuální okno.
        """
        self.root.destroy()
