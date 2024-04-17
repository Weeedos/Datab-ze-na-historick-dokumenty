import tkinter
from tkinter import messagebox


class LetterDeleteUI:
    def __init__(self, root, letter):
        self.letter = letter
        self.root = root
        self.root.title("Odebrat dopis")

        self.label_sender = tkinter.Label(root, text="Odesílatel:")
        self.label_sender.grid(row=0, column=0, padx=10, pady=5, sticky='we')
        self.entry_sender = tkinter.Entry(root)
        self.entry_sender.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.label_recipient = tkinter.Label(root, text="Příjemce:")
        self.label_recipient.grid(row=1, column=0, padx=10, pady=5, sticky='we')
        self.entry_recipient = tkinter.Entry(root)
        self.entry_recipient.grid(row=1, column=1, padx=10, pady=5, sticky='we')

        self.button_delete = tkinter.Button(root, text="Odebrat", command=self.delete)
        self.button_delete.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def delete(self):
        sender = self.entry_sender.get()
        recipient = self.entry_recipient.get()

        self.letter.delete_from_letter(sender, recipient)

        messagebox.showinfo("Úspěch", "Úspěšně odebráno.")

    def back(self):
        self.root.destroy()
