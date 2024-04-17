import tkinter
from tkinter import messagebox


class BookUpdateMenuUI:
    """
    Reprezentuje uživatelské rozhraní pro úpravu informací o knize v databázi.
    """
    def __init__(self, root, book, id):
        """
        Inicializuje objekt rozhraní BookUpdateMenuUI.
        """
        self.book = book
        self.root = root
        self.id = id
        self.root.title("Upravit knihu")

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

        self.button_update = tkinter.Button(root, text="Upravit", command=self.update)
        self.button_update.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def update(self):
        """
        Aktualizuje informace o knize na základě zadaných hodnot a zobrazí zprávu o úspěchu.
        """
        title = self.entry_title.get()
        publication_date = self.entry_publication_date.get()
        genre = self.entry_genre.get()
        author = self.entry_author.get()
        language = self.entry_language.get()
        isbn = self.entry_isbn.get()

        if not all([title, publication_date, genre, author, language, isbn]):
            messagebox.showerror("Chyba", "Všechna pole musí být vyplněna.")
            return

        try:
            self.book.update_book(self.id, title, author, publication_date, genre, language, isbn)
            messagebox.showinfo("Úspěch", "Úspěšně upraveno.")
            self.back()
        except Exception as e:
            messagebox.showerror("Chyba", f"Nastala chyba při aktualizaci: {str(e)}")

    def back(self):
        """
        Zavře okno aktualizace.
        """
        self.root.destroy()
