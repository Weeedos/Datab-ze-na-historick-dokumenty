import tkinter
from tkinter import messagebox, ttk
from src.speech.speechUpdateMenuUI import SpeechUpdateMenuUI


class SpeechUpdateUI:
    """
    Třída SpeechUpdateUI poskytuje uživatelské rozhraní pro aktualizaci existujících projevů.
    """

    def __init__(self, root, speech):
        """
        Inicializuje novou instanci třídy SpeechUpdateUI.
        """
        self.root = root
        self.speech = speech
        self.root.title("Úprava")

        self.button_refresh = tkinter.Button(self.root, text="Obnovit", command=self.refresh)
        self.button_refresh.grid(row=0, column=0, padx=10, pady=5, sticky='we')

        self.label_id = tkinter.Label(self.root)
        self.label_id.grid(row=0, column=1, padx=10, pady=5, sticky='we')
        self.entry_id = tkinter.Entry(self.root)
        self.entry_id.grid(row=0, column=2, padx=10, pady=5, sticky='we')

        self.button_update = tkinter.Button(self.root, text="Upravit", command=self.update)
        self.button_update.grid(row=0, column=3, padx=10, pady=5, sticky='we')

        self.result_tree = ttk.Treeview(self.root, columns=("ID", "Název", "Autor", "Datum", "Obsah"),
                                        show="headings")
        self.result_tree.heading("ID", text="ID")
        self.result_tree.heading("Název", text="Název")
        self.result_tree.heading("Autor", text="Autor")
        self.result_tree.heading("Datum", text="Datum (RRRR-MM-DD)")
        self.result_tree.heading("Obsah", text="Obsah")
        self.result_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='we')

        self.button_back = tkinter.Button(self.root, text="Zpět", command=self.back)
        self.button_back.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='we')

        self.refresh()

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def update(self):
        """
        Otevře nové okno pro úpravu vybraného projevu.
        """
        id = self.entry_id.get()
        select_id = self.speech.select_from_speech_by_id(id)

        if not select_id:
            messagebox.showerror("Chyba", "Záznam se zadaným ID neexistuje.")
            raise Exception("Záznam se zadaným ID neexistuje.")

        update_id_root = tkinter.Tk()
        SpeechUpdateMenuUI(update_id_root, self.speech, id)
        update_id_root.mainloop()

    def refresh(self):
        """
        Obnoví seznam všech projevů v rozhraní.
        """
        self.result_tree.delete(*self.result_tree.get_children())

        for result in self.speech.select_all():
            self.result_tree.insert("", "end", values=result)

    def back(self):
        """
        Ukončí práci s rozhraním a zavře okno.
        """
        self.root.destroy()
