import tkinter
from tkinter import messagebox


class DiaryUpdateMenuUI:
    """
    Třída DiaryUpdateMenuUI reprezentuje uživatelské rozhraní pro úpravu existujícího deníkového záznamu.
    """

    def __init__(self, root, diary, id):
        """
        Inicializuje novou instanci třídy DiaryUpdateMenuUI.
        """
        self.diary = diary
        self.root = root
        self.id = id
        self.root.title("Upravit deník")

        self.label_title = tkinter.Label(root, text="Název:")
        self.label_title.grid(row=0, column=0, padx=10, pady=5, sticky='we')
        self.entry_title = tkinter.Entry(root)
        self.entry_title.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.label_author = tkinter.Label(root, text="Autor:")
        self.label_author.grid(row=1, column=0, padx=10, pady=5, sticky='we')
        self.entry_author = tkinter.Entry(root)
        self.entry_author.grid(row=1, column=1, padx=10, pady=5, sticky='we')

        self.label_date = tkinter.Label(root, text="Datum (RRRR-MM-DD):")
        self.label_date.grid(row=2, column=0, padx=10, pady=5, sticky='we')
        self.entry_date = tkinter.Entry(root)
        self.entry_date.grid(row=2, column=1, padx=10, pady=5, sticky='we')

        self.label_content = tkinter.Label(root, text="Obsah:")
        self.label_content.grid(row=3, column=0, padx=10, pady=5, sticky='we')
        self.entry_content = tkinter.Entry(root)
        self.entry_content.grid(row=3, column=1, padx=10, pady=5, sticky='we')

        self.button_update = tkinter.Button(root, text="Upravit", command=self.update)
        self.button_update.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def update(self):
        """
        Aktualizuje existující deníkový záznam s novými hodnotami.
        """
        title = self.entry_title.get()
        date = self.entry_date.get()
        content = self.entry_content.get()
        autor = self.entry_author.get()

        if title is None or title == " ":
            messagebox.showerror("Chyba", f"Nezadali jste název.")
            raise Exception("Nezadali jste název.")
        elif date is None or date == " ":
            messagebox.showerror("Chyba", f"Nezadali jste datum.")
            raise Exception("Nezadali jste datum.")
        elif content is None or content == " ":
            messagebox.showerror("Chyba", f"Nezadali jste obsah.")
            raise Exception("Nezadali jste obsah.")
        elif autor is None or autor == " ":
            messagebox.showerror("Chyba", f"Nezadali jste autora.")
            raise Exception("Nezadali jste autora.")

        self.diary.update_diary(self.id, title, autor, date, content)

        messagebox.showinfo("Úspěch", "Úspěšně upraveno.")
        self.back()

    def back(self):
        """
        Zavře okno pro úpravu deníkového záznamu.
        """
        self.root.destroy()
