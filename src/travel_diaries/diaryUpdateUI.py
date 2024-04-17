import tkinter
from tkinter import ttk, messagebox
from src.travel_diaries.diaryUpdateMenuUI import DiaryUpdateMenuUI


class DiaryUpdateUI:
    """
    Třída DiaryUpdateUI reprezentuje uživatelské rozhraní pro výběr a úpravu existujícího deníkového záznamu.
    """

    def __init__(self, root, diary):
        """
        Inicializuje novou instanci třídy DiaryUpdateUI.
        """
        self.root = root
        self.diary = diary
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
        Zobrazí uživatelské rozhraní pro úpravu vybraného deníkového záznamu.
        """
        id = self.entry_id.get()
        select_id = self.diary.select_from_diary_by_id(id)

        if not select_id:
            messagebox.showerror("Chyba", "Záznam se zadaným ID neexistuje.")
            raise Exception("Záznam se zadaným ID neexistuje.")

        update_id_root = tkinter.Tk()
        DiaryUpdateMenuUI(update_id_root, self.diary, id)
        update_id_root.mainloop()

    def refresh(self):
        """
        Obnoví seznam deníkových záznamů v uživatelském rozhraní.
        """
        self.result_tree.delete(*self.result_tree.get_children())

        for result in self.diary.select_all():
            self.result_tree.insert("", "end", values=result)

    def back(self):
        """
        Zavře okno pro úpravu deníkového záznamu.
        """
        self.root.destroy()
