import tkinter
from tkinter import ttk, messagebox
from src.letter.letterUpdateMenuUI import LetterUpdateMenuUI


class LetterUpdateUI:
    """
    Třída LetterUpdateUI poskytuje uživatelské rozhraní pro aktualizaci dopisu v databázi.
    """
    def __init__(self, root, letter):
        """
        Inicializuje uživatelské rozhraní pro aktualizaci dopisu.

        Args:
            root: Tkinter kořenové okno.
            letter: Instance třídy pro manipulaci s dopisy.
        """
        self.root = root
        self.letter = letter
        self.root.title("Úprava")

        self.button_refresh = tkinter.Button(self.root, text="Obnovit", command=self.refresh)
        self.button_refresh.grid(row=0, column=0, padx=10, pady=5, sticky='we')

        self.label_id = tkinter.Label(self.root, text="ID:")
        self.label_id.grid(row=0, column=1, padx=10, pady=5, sticky='we')
        self.entry_id = tkinter.Entry(self.root)
        self.entry_id.grid(row=0, column=2, padx=10, pady=5, sticky='we')

        self.button_update = tkinter.Button(self.root, text="Upravit", command=self.update)
        self.button_update.grid(row=0, column=3, padx=10, pady=5, sticky='we')

        self.result_tree = ttk.Treeview(self.root, columns=("ID", "Odesílatel", "Příjemce", "Datum odeslání", "Obsah"),
                                        show="headings")
        self.result_tree.heading("ID", text="ID")
        self.result_tree.heading("Odesílatel", text="Odesílatel")
        self.result_tree.heading("Příjemce", text="Příjemce")
        self.result_tree.heading("Datum odeslání", text="Datum odeslání (RRRR-MM-DD)")
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
        Zahájí proces aktualizace dopisu.
        """
        id = self.entry_id.get()
        select_id = self.letter.select_from_letter_by_id(id)

        if not select_id:
            messagebox.showerror("Chyba", "Záznam se zadaným ID neexistuje.")
            return

        update_id_root = tkinter.Tk()
        LetterUpdateMenuUI(update_id_root, self.letter, id)
        update_id_root.mainloop()

    def refresh(self):
        """
        Aktualizuje seznam dopisů.
        """
        self.result_tree.delete(*self.result_tree.get_children())

        for result in self.letter.select_all():
            self.result_tree.insert("", "end", values=result)

    def back(self):
        """
        Zavře okno.
        """
        self.root.destroy()
