import tkinter
from tkinter import ttk, messagebox
from src.charter.charterUpdateMenuUI import CharterUpdateMenuUI


class CharterUpdateUI:
    """
    Uživatelské rozhraní pro výběr listiny k úpravě.
    """
    def __init__(self, root, charter):
        """
        Inicializuje uživatelské rozhraní pro výběr listiny k úpravě.
        """
        self.root = root
        self.charter = charter
        self.root.title("Úprava")

        self.button_refresh = tkinter.Button(self.root, text="Obnovit", command=self.refresh)
        self.button_refresh.grid(row=0, column=0, padx=10, pady=5, sticky='we')

        self.label_id = tkinter.Label(self.root)
        self.label_id.grid(row=0, column=1, padx=10, pady=5, sticky='we')
        self.entry_id = tkinter.Entry(self.root)
        self.entry_id.grid(row=0, column=2, padx=10, pady=5, sticky='we')

        self.button_update = tkinter.Button(self.root, text="Upravit", command=self.update)
        self.button_update.grid(row=0, column=3, padx=10, pady=5, sticky='we')

        self.result_tree = ttk.Treeview(self.root, columns=("ID", "Název", "Autor", "Období", "Země", "Datum vydání"),
                                        show="headings")
        self.result_tree.heading("ID", text="ID")
        self.result_tree.heading("Název", text="Název")
        self.result_tree.heading("Autor", text="Autor")
        self.result_tree.heading("Období", text="Období")
        self.result_tree.heading("Země", text="Země")
        self.result_tree.heading("Datum vydání", text="Datum vydání (RRRR-MM-DD)")
        self.result_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='we')

        self.button_back = tkinter.Button(self.root, text="Zpět", command=self.back)
        self.button_back.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='we')

        self.refresh()

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def update(self):
        """
        Získá vybrané ID listiny a spustí rozhraní pro úpravu listiny.
        """
        id = self.entry_id.get()
        select_id = self.charter.select_from_charter_by_id(id)

        if not select_id:
            messagebox.showerror("Chyba", "Záznam se zadaným ID neexistuje.")
            return

        charter_update_id_root = tkinter.Tk()
        CharterUpdateMenuUI(charter_update_id_root, self.charter, id)
        charter_update_id_root.mainloop()

    def refresh(self):
        """
        Obnoví seznam všech listin v Treeview.
        """
        self.result_tree.delete(*self.result_tree.get_children())
        for result in self.charter.select_all():
            self.result_tree.insert("", "end", values=result)

    def back(self):
        """
        Zavře aktuální okno.
        """
        self.root.destroy()
