import tkinter
from tkinter import messagebox


class LetterInsertUI:
    """
    Třída LetterInsertUI poskytuje uživatelské rozhraní pro přidání nového dopisu do databáze.
    """
    def __init__(self, root, letter):
        """
        Inicializuje uživatelské rozhraní pro vložení dopisu.
        """
        self.letter = letter
        self.root = root
        self.root.title("Přidat dopis")

        self.label_sender = tkinter.Label(root, text="Odesílatel:")
        self.label_sender.grid(row=0, column=0, padx=10, pady=5, sticky='we')
        self.entry_sender = tkinter.Entry(root)
        self.entry_sender.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.label_recipient = tkinter.Label(root, text="Příjemce:")
        self.label_recipient.grid(row=1, column=0, padx=10, pady=5, sticky='we')
        self.entry_recipient = tkinter.Entry(root)
        self.entry_recipient.grid(row=1, column=1, padx=10, pady=5, sticky='we')

        self.label_sending_date = tkinter.Label(root, text="Datum odeslání (RRRR-MM-DD):")
        self.label_sending_date.grid(row=2, column=0, padx=10, pady=5, sticky='we')
        self.entry_sending_date = tkinter.Entry(root)
        self.entry_sending_date.grid(row=2, column=1, padx=10, pady=5, sticky='we')

        self.label_content = tkinter.Label(root, text="Obsah:")
        self.label_content.grid(row=3, column=0, padx=10, pady=5, sticky='we')
        self.entry_content = tkinter.Entry(root)
        self.entry_content.grid(row=3, column=1, padx=10, pady=5, sticky='we')

        self.button_insert = tkinter.Button(root, text="Vložit", command=self.insert)
        self.button_insert.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=4, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def insert(self):
        """
        Vloží nový dopis do databáze.
        """
        sender = self.entry_sender.get()
        recipient = self.entry_recipient.get()
        sending_date = self.entry_sending_date.get()
        content = self.entry_content.get()

        self.letter.insert_into_letter(sender, recipient, sending_date, content)

        messagebox.showinfo("Úspěch", "Úspěšně přidáno.")

    def back(self):
        """
        Zavře okno.
        """
        self.root.destroy()
