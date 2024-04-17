import tkinter
from tkinter import messagebox


class ChronicleInsertUI:
    """
    Třída pro vytvoření uživatelského rozhraní pro přidání nové kroniky.
    """
    def __init__(self, root, chronicle):
        """
        Inicializuje uživatelské rozhraní pro přidání nové kroniky.

        :param root: Hlavní okno aplikace.
        :param chronicle: Instance třídy Chronicle pro manipulaci s kronikami v databázi.
        """
        self.chronicle = chronicle
        self.root = root
        self.root.title("Přidat kroniku")

        self.label_title = tkinter.Label(root, text="Název:")
        self.label_title.grid(row=0, column=0, padx=10, pady=5, sticky='we')
        self.entry_title = tkinter.Entry(root)
        self.entry_title.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.label_author = tkinter.Label(root, text="Autor:")
        self.label_author.grid(row=3, column=0, padx=10, pady=5, sticky='we')
        self.entry_author = tkinter.Entry(root)
        self.entry_author.grid(row=3, column=1, padx=10, pady=5, sticky='we')

        self.label_publication_date = tkinter.Label(root, text="Datum vydání (RRRR-MM-DD):")
        self.label_publication_date.grid(row=1, column=0, padx=10, pady=5, sticky='we')
        self.entry_publication_date = tkinter.Entry(root)
        self.entry_publication_date.grid(row=1, column=1, padx=10, pady=5, sticky='we')

        self.label_genre = tkinter.Label(root, text="Žánr:")
        self.label_genre.grid(row=2, column=0, padx=10, pady=5, sticky='we')
        self.entry_genre = tkinter.Entry(root)
        self.entry_genre.grid(row=2, column=1, padx=10, pady=5, sticky='we')

        self.label_language = tkinter.Label(root, text="Jazyk:")
        self.label_language.grid(row=4, column=0, padx=10, pady=5, sticky='we')
        self.entry_language = tkinter.Entry(root)
        self.entry_language.grid(row=4, column=1, padx=10, pady=5, sticky='we')

        self.button_insert = tkinter.Button(root, text="Vložit", command=self.insert)
        self.button_insert.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def insert(self):
        """
        Odešle požadavek na vložení nové kroniky do databáze.
        """
        title = self.entry_title.get()
        publication_date = self.entry_publication_date.get()
        genre = self.entry_genre.get()
        author = self.entry_author.get()
        language = self.entry_language.get()

        self.chronicle.insert_into_chronicle(title, author, publication_date, genre, language)

        messagebox.showinfo("Úspěch", "Úspěšně přidáno.")

    def back(self):
        """
        Zavře okno a vrátí se zpět.
        """
        self.root.destroy()
