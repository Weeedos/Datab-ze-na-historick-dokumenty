import tkinter
from tkinter import messagebox


class ReligionUpdateMenuUI:
    """
    Třída ReligionUpdateMenuUI poskytuje uživatelské rozhraní pro aktualizaci informací o náboženském textu v databázi.
    """

    def __init__(self, root, religion, id):
        """
        Inicializuje novou instanci třídy ReligionUpdateMenuUI.
        """
        self.religion = religion
        self.root = root
        self.id = id
        self.root.title("Upravit náboženský text")

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

        self.label_description = tkinter.Label(root, text="Popis:")
        self.label_description.grid(row=2, column=0, padx=10, pady=5, sticky='we')
        self.entry_description = tkinter.Entry(root)
        self.entry_description.grid(row=2, column=1, padx=10, pady=5, sticky='we')

        self.label_language = tkinter.Label(root, text="Jazyk:")
        self.label_language.grid(row=4, column=0, padx=10, pady=5, sticky='we')
        self.entry_language = tkinter.Entry(root)
        self.entry_language.grid(row=4, column=1, padx=10, pady=5, sticky='we')

        self.button_update = tkinter.Button(root, text="Upravit", command=self.update)
        self.button_update.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def update(self):
        """
        Aktualizuje informace o náboženském textu na základě zadaných údajů.
        """
        title = self.entry_title.get()
        publication_date = self.entry_publication_date.get()
        description = self.entry_description.get()
        author = self.entry_author.get()
        language = self.entry_language.get()

        if title is None or title == " ":
            messagebox.showerror("Chyba", f"Nezadali jste název.")
            raise Exception("Nezadali jste název.")
        if publication_date is None or publication_date == " ":
            messagebox.showerror("Chyba", f"Nezadali jste datum.")
            raise Exception("Nezadali jste datum.")
        if description is None or description == " ":
            messagebox.showerror("Chyba", f"Nezadali jste obsah.")
            raise Exception("Nezadali jste obsah.")
        if author is None or author == " ":
            messagebox.showerror("Chyba", f"Nezadali jste autora.")
            raise Exception("Nezadali jste autora.")
        if language is None or language == " ":
            messagebox.showerror("Chyba", f"Nezadali jste stát.")
            raise Exception("Nezadali jste stát.")

        self.religion.update_religion(self.id, title, author, publication_date, description, language)

        messagebox.showinfo("Úspěch", "Úspěšně upraveno.")
        self.back()

    def back(self):
        """
        Zavře aktuální okno.
        """
        self.root.destroy()
