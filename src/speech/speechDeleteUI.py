import tkinter
from tkinter import messagebox


class SpeechDeleteUI:
    """
    Třída SpeechDeleteUI poskytuje uživatelské rozhraní pro odstranění záznamu řeči.
    """

    def __init__(self, root, speech):
        """
        Inicializuje novou instanci třídy SpeechDeleteUI.
        """
        self.speech = speech
        self.root = root
        self.root.title("Odebrat dopis")

        self.label_title = tkinter.Label(root, text="Název:")
        self.label_title.grid(row=0, column=0, padx=10, pady=5, sticky='we')
        self.entry_title = tkinter.Entry(root)
        self.entry_title.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.button_delete = tkinter.Button(root, text="Odebrat", command=self.delete)
        self.button_delete.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=1, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def delete(self):
        """
        Odebere záznam řeči z databáze.
        """
        title = self.entry_title.get()
        self.speech.delete_from_speech(title)
        messagebox.showinfo("Úspěch", "Úspěšně odebráno.")

    def back(self):
        """
        Ukončí práci s rozhraním a zavře okno.
        """
        self.root.destroy()
