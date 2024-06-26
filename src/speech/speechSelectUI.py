import tkinter
from tkinter import ttk


class SpeechSelectUI:
    """
    Třída SpeechSelectUI poskytuje uživatelské rozhraní pro vyhledávání záznamů řečí.
    """

    def __init__(self, root, speech):
        """
        Inicializuje novou instanci třídy SpeechSelectUI.
        """
        self.root = root
        self.speech = speech
        self.root.title("Vyhledávání")

        self.label_search = tkinter.Label(self.root, text="Hledat podle:")
        self.label_search.grid(row=0, column=0, padx=10, pady=5, sticky='we')

        self.search_options = ["Název", "Autor", "Datum", "Obsah"]
        self.search_var = tkinter.StringVar(self.root)
        self.search_var.set(self.search_options[0])
        self.search_dropdown = ttk.Combobox(self.root, textvariable=self.search_var, values=self.search_options)
        self.search_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.entry_search = tkinter.Entry(self.root)
        self.entry_search.grid(row=0, column=2, padx=10, pady=5, sticky='we')

        self.button_search = tkinter.Button(self.root, text="Hledat", command=self.search)
        self.button_search.grid(row=0, column=3, padx=10, pady=5, sticky='we')

        self.result_tree = ttk.Treeview(self.root, columns=("Název", "Autor", "Datum", "Obsah"),
                                        show="headings")
        self.result_tree.heading("Název", text="Název")
        self.result_tree.heading("Autor", text="Autor")
        self.result_tree.heading("Datum", text="Datum (RRRR-MM-DD)")
        self.result_tree.heading("Obsah", text="Obsah")
        self.result_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='we')

        self.button_back = tkinter.Button(self.root, text="Zpět", command=self.back)
        self.button_back.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def search(self):
        """
        Provede vyhledávání záznamů podle zadaných kritérií.
        """
        search_by = self.search_var.get()
        search_term = self.entry_search.get()
        self.result_tree.delete(*self.result_tree.get_children())

        if search_by == "Název":
            results = self.speech.select_from_speech_by_title(search_term)
        elif search_by == "Autor":
            results = self.speech.select_from_speech_by_author(search_term)
        elif search_by == "Datum":
            results = self.speech.select_from_speech_by_publication_date(search_term)
        elif search_by == "Obsah":
            results = self.speech.select_from_speech_by_content(search_term)

        if results is None:
            return

        for result in results:
            self.result_tree.insert("", "end", values=result[1:])

    def back(self):
        """
        Ukončí práci s rozhraním a zavře okno.
        """
        self.root.destroy()
