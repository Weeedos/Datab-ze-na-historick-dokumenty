import tkinter
from tkinter import messagebox


class ReligionDeleteUI:
    """
    Třída ReligionDeleteUI poskytuje uživatelské rozhraní pro odstranění náboženského textu z databáze.
    """

    def __init__(self, root, religion):
        """
        Inicializuje novou instanci třídy ReligionDeleteUI.
        """
        self.religion = religion
        self.root = root
        self.root.title("Odebrat náboženský text")

        self.label_title = tkinter.Label(root, text="Název:")
        self.label_title.grid(row=0, column=0, padx=10, pady=5, sticky='we')
        self.entry_title = tkinter.Entry(root)
        self.entry_title.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.button_delete = tkinter.Button(root, text="Odebrat", command=self.delete)
        self.button_delete.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def delete(self):
        """
        Odebere náboženský text z databáze na základě zadaného názvu.
        """
        title = self.entry_title.get()

        self.religion.delete_from_religion(title)

        messagebox.showinfo("Úspěch", "Úspěšně odebráno.")

    def back(self):
        """
        Zavře aktuální okno.
        """
        self.root.destroy()
