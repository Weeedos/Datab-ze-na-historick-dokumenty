import tkinter
from tkinter import messagebox


class BookInsertUI:
    """
    Reprezentuje uživatelské rozhraní pro přidání knihy do databáze.
    """
    def __init__(self, root, book):
        """
        Inicializuje objekt rozhraní BookInsertUI.
        """
        self.book = book
        self.root = root
        self.root.title("Přidat knihu")

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

        self.label_isbn = tkinter.Label(root, text="ISBN:")
        self.label_isbn.grid(row=5, column=0, padx=10, pady=5, sticky='we')
        self.entry_isbn = tkinter.Entry(root)
        self.entry_isbn.grid(row=5, column=1, padx=10, pady=5, sticky='we')

        self.button_insert = tkinter.Button(root, text="Vložit", command=self.insert)
        self.button_insert.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def insert(self):
        """
        Spustí proces přidání knihy do databáze na základě zadaných informací uživatelem.
        """
        title = self.entry_title.get()
        publication_date = self.entry_publication_date.get()
        genre = self.entry_genre.get()
        author = self.entry_author.get()
        language = self.entry_language.get()
        isbn = self.entry_isbn.get()

        self.book.insert_into_book(title, author, publication_date, genre, language, isbn)

        messagebox.showinfo("Úspěch", "Úspěšně přidáno.")

    def back(self):
        """
        Ukončí práci s rozhraním a zavře ho.
        """
        self.root.destroy()
