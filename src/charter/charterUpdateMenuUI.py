import tkinter
from tkinter import messagebox


class CharterUpdateMenuUI:
    """
    Uživatelské rozhraní pro úpravu informací o listině.
    """
    def __init__(self, root, charter, id):
        """
        Inicializuje uživatelské rozhraní pro úpravu informací o listině.
        """
        self.charter = charter
        self.root = root
        self.id = id
        self.root.title("Upravit listinu")

        self.label_title = tkinter.Label(root, text="Název:")
        self.label_title.grid(row=0, column=0, padx=10, pady=5, sticky='we')
        self.entry_title = tkinter.Entry(root)
        self.entry_title.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.label_issuance_date = tkinter.Label(root, text="Datum vydání (RRRR-MM-DD):")
        self.label_issuance_date.grid(row=1, column=0, padx=10, pady=5, sticky='we')
        self.entry_issuance_date = tkinter.Entry(root)
        self.entry_issuance_date.grid(row=1, column=1, padx=10, pady=5, sticky='we')

        self.label_content = tkinter.Label(root, text="Obsah:")
        self.label_content.grid(row=2, column=0, padx=10, pady=5, sticky='we')
        self.entry_content = tkinter.Entry(root)
        self.entry_content.grid(row=2, column=1, padx=10, pady=5, sticky='we')

        self.label_author = tkinter.Label(root, text="Autor:")
        self.label_author.grid(row=3, column=0, padx=10, pady=5, sticky='we')
        self.entry_author = tkinter.Entry(root)
        self.entry_author.grid(row=3, column=1, padx=10, pady=5, sticky='we')

        self.label_country = tkinter.Label(root, text="Stát:")
        self.label_country.grid(row=4, column=0, padx=10, pady=5, sticky='we')
        self.entry_country = tkinter.Entry(root)
        self.entry_country.grid(row=4, column=1, padx=10, pady=5, sticky='we')

        self.label_period = tkinter.Label(root, text="Období:")
        self.label_period.grid(row=5, column=0, padx=10, pady=5, sticky='we')
        self.entry_period = tkinter.Entry(root)
        self.entry_period.grid(row=5, column=1, padx=10, pady=5, sticky='we')

        self.button_update = tkinter.Button(root, text="Upravit", command=self.update)
        self.button_update.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def update(self):
        """
        Aktualizuje informace o listině na základě vstupů z uživatelského rozhraní.
        """
        title = self.entry_title.get()
        issuance_date = self.entry_issuance_date.get()
        content = self.entry_content.get()
        author = self.entry_author.get()
        country = self.entry_country.get()
        period = self.entry_period.get()

        if title is None or title == " ":
            messagebox.showerror("Chyba", f"Nezadali jste název.")
            raise Exception("Nezadali jste název.")
        if issuance_date is None or issuance_date == " ":
            messagebox.showerror("Chyba", f"Nezadali jste datum.")
            raise Exception("Nezadali jste datum.")
        if content is None or content == " ":
            messagebox.showerror("Chyba", f"Nezadali jste obsah.")
            raise Exception("Nezadali jste obsah.")
        if author is None or author == " ":
            messagebox.showerror("Chyba", f"Nezadali jste autora.")
            raise Exception("Nezadali jste autora.")
        if country is None or country == " ":
            messagebox.showerror("Chyba", f"Nezadali jste stát.")
            raise Exception("Nezadali jste stát.")
        if period is None or period == " ":
            messagebox.showerror("Chyba", f"Nezadali jste období.")
            raise Exception("Nezadali jste období.")

        self.charter.update_charter(self.id, title, issuance_date, content, author, country, period)

        messagebox.showinfo("Úspěch", "Úspěšně upraveno.")
        self.back()

    def back(self):
        """
        Uzavře aktuální okno.
        """
        self.root.destroy()
