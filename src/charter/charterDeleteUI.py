import tkinter
from tkinter import messagebox


class CharterDeleteUI:
    """
    Uživatelské rozhraní pro odebrání listiny.
    """
    def __init__(self, root, charter):
        """
        Inicializuje uživatelské rozhraní pro odebrání listiny.
        """
        self.charter = charter
        self.root = root
        self.root.title("Odebrat listinu")

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
        Odebere listinu z databáze na základě zadaného názvu.
        """
        title = self.entry_title.get()

        self.charter.delete_from_charter(title)

        messagebox.showinfo("Úspěch", "Úspěšně odebráno.")

    def back(self):
        """
        Uzavírá aktuální okno.
        """
        self.root.destroy()
