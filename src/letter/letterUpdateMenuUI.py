import tkinter
from tkinter import messagebox


class LetterUpdateMenuUI:
    def __init__(self, root, letter, id):
        self.letter = letter
        self.root = root
        self.id = id
        self.root.title("Upravit dopis")

        self.label_sender = tkinter.Label(root, text="Odesílatel:")
        self.label_sender.grid(row=0, column=0, padx=10, pady=5)
        self.entry_sender = tkinter.Entry(root)
        self.entry_sender.grid(row=0, column=1, padx=10, pady=5)

        self.label_recipient = tkinter.Label(root, text="Příjemce:")
        self.label_recipient.grid(row=1, column=0, padx=10, pady=5)
        self.entry_recipient = tkinter.Entry(root)
        self.entry_recipient.grid(row=1, column=1, padx=10, pady=5)

        self.label_sending_date = tkinter.Label(root, text="Datum odeslání (RRRR-MM-DD):")
        self.label_sending_date.grid(row=2, column=0, padx=10, pady=5)
        self.entry_sending_date = tkinter.Entry(root)
        self.entry_sending_date.grid(row=2, column=1, padx=10, pady=5)

        self.label_content = tkinter.Label(root, text="Obsah:")
        self.label_content.grid(row=3, column=0, padx=10, pady=5)
        self.entry_content = tkinter.Entry(root)
        self.entry_content.grid(row=3, column=1, padx=10, pady=5)

        self.button_update = tkinter.Button(root, text="Upravit", command=self.update)
        self.button_update.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10)

    def update(self):
        sender = self.entry_sender.get()
        sending_date = self.entry_sending_date.get()
        content = self.entry_content.get()
        recipient = self.entry_recipient.get()

        if sender is None or sender == " ":
            messagebox.showerror("Chyba", f"Nezadali jste odesílatele.")
            raise Exception("Nezadali jste odesílatele.")
        elif sending_date is None or sending_date == " ":
            messagebox.showerror("Chyba", f"Nezadali jste datum.")
            raise Exception("Nezadali jste datum.")
        elif content is None or content == " ":
            messagebox.showerror("Chyba", f"Nezadali jste obsah.")
            raise Exception("Nezadali jste obsah.")
        elif recipient is None or recipient == " ":
            messagebox.showerror("Chyba", f"Nezadali jste přijemce.")
            raise Exception("Nezadali jste přijemce.")

        self.letter.update_letter(self.id, sender, recipient, sending_date, content)

        messagebox.showinfo("Úspěch", "Úspěšně upraveno.")
        self.back()

    def back(self):
        self.root.destroy()
