import tkinter
from tkinter import ttk, messagebox
from src.charter.charterUpdateMenuUI import CharterUpdateMenuUI


class CharterUpdateUI:
    def __init__(self, root, charter):
        self.root = root
        self.charter = charter
        self.root.title("Úprava")

        self.button_refresh = tkinter.Button(self.root, text="Obnovit", command=self.refresh)
        self.button_refresh.grid(row=0, column=0, padx=10, pady=5)

        self.label_id = tkinter.Label(self.root)
        self.label_id.grid(row=0, column=1, padx=10, pady=5)
        self.entry_id = tkinter.Entry(self.root)
        self.entry_id.grid(row=0, column=2, padx=10, pady=5)

        self.button_update = tkinter.Button(self.root, text="Upravit", command=self.update)
        self.button_update.grid(row=0, column=3, padx=10, pady=5)

        self.result_tree = ttk.Treeview(self.root, columns=("ID", "Název", "Autor", "Období", "Země", "Datum vydání"),
                                        show="headings")
        self.result_tree.heading("ID", text="ID")
        self.result_tree.heading("Název", text="Název")
        self.result_tree.heading("Autor", text="Autor")
        self.result_tree.heading("Období", text="Období")
        self.result_tree.heading("Země", text="Země")
        self.result_tree.heading("Datum vydání", text="Datum vydání (RRRR-MM-DD)")
        self.result_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

        self.button_back = tkinter.Button(self.root, text="Zpět", command=self.back)
        self.button_back.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.refresh()

    def update(self):
        id = self.entry_id.get()
        select_id = self.charter.select_from_charter_by_id(id)

        if not select_id:
            messagebox.showerror("Chyba", "Záznam se zadaným ID neexitsuje.")
            raise Exception("Záznam se zadaným ID neexitsuje.")

        charter_update_id_root = tkinter.Tk()
        CharterUpdateMenuUI(charter_update_id_root, self.charter, id)
        charter_update_id_root.mainloop()

    def refresh(self):
        self.result_tree.delete(*self.result_tree.get_children())

        for result in self.charter.select_all():
            self.result_tree.insert("", "end", values=result)

    def back(self):
        self.root.destroy()
