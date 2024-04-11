import tkinter
from tkinter import messagebox


class BookUpdateMenuUI:
    def __init__(self, root, book, id):
        self.book = book
        self.root = root
        self.id = id
        self.root.title("Upravit knihu")

        self.label_title = tkinter.Label(root, text="Název:")
        self.label_title.grid(row=0, column=0, padx=10, pady=5)
        self.entry_title = tkinter.Entry(root)
        self.entry_title.grid(row=0, column=1, padx=10, pady=5)

        self.label_author = tkinter.Label(root, text="Autor:")
        self.label_author.grid(row=3, column=0, padx=10, pady=5)
        self.entry_author = tkinter.Entry(root)
        self.entry_author.grid(row=3, column=1, padx=10, pady=5)

        self.label_publication_date = tkinter.Label(root, text="Datum vydání (RRRR-MM-DD):")
        self.label_publication_date.grid(row=1, column=0, padx=10, pady=5)
        self.entry_publication_date = tkinter.Entry(root)
        self.entry_publication_date.grid(row=1, column=1, padx=10, pady=5)

        self.label_genre = tkinter.Label(root, text="Žánr:")
        self.label_genre.grid(row=2, column=0, padx=10, pady=5)
        self.entry_genre = tkinter.Entry(root)
        self.entry_genre.grid(row=2, column=1, padx=10, pady=5)

        self.label_language = tkinter.Label(root, text="Jazyk:")
        self.label_language.grid(row=4, column=0, padx=10, pady=5)
        self.entry_language = tkinter.Entry(root)
        self.entry_language.grid(row=4, column=1, padx=10, pady=5)

        self.label_isbn = tkinter.Label(root, text="ISBN:")
        self.label_isbn.grid(row=5, column=0, padx=10, pady=5)
        self.entry_isbn = tkinter.Entry(root)
        self.entry_isbn.grid(row=5, column=1, padx=10, pady=5)

        self.button_update = tkinter.Button(root, text="Upravit", command=self.update)
        self.button_update.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10)

    def update(self):
        title = self.entry_title.get()
        publication_date = self.entry_publication_date.get()
        genre = self.entry_genre.get()
        author = self.entry_author.get()
        language = self.entry_language.get()
        isbn = self.entry_isbn.get()

        if title is None or title == " ":
            messagebox.showerror("Chyba", f"Nezadali jste název.")
            raise Exception("Nezadali jste název.")
        if publication_date is None or publication_date == " ":
            messagebox.showerror("Chyba", f"Nezadali jste datum.")
            raise Exception("Nezadali jste datum.")
        if genre is None or genre == " ":
            messagebox.showerror("Chyba", f"Nezadali jste obsah.")
            raise Exception("Nezadali jste obsah.")
        if author is None or author == " ":
            messagebox.showerror("Chyba", f"Nezadali jste autora.")
            raise Exception("Nezadali jste autora.")
        if language is None or language == " ":
            messagebox.showerror("Chyba", f"Nezadali jste stát.")
            raise Exception("Nezadali jste stát.")
        if isbn is None or isbn == " ":
            messagebox.showerror("Chyba", f"Nezadali jste období.")
            raise Exception("Nezadali jste období.")

        self.book.update_book(self.id, title, author, publication_date, genre, language, isbn)

        messagebox.showinfo("Úspěch", "Úspěšně upraveno.")
        self.back()

    def back(self):
        self.root.destroy()
