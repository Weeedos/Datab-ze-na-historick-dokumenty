import tkinter
from tkinter import messagebox


class DiaryDeleteUI:
    """
    Třída DiaryDeleteUI reprezentuje uživatelské rozhraní pro odstranění deníkového záznamu.

    Attributes:
        diary: Instance třídy Diary pro manipulaci s deníkovými záznamy.
        root: Hlavní okno aplikace.

    Methods:
        __init__(root, diary): Inicializuje novou instanci třídy DiaryDeleteUI.
        delete(): Odstraní deníkový záznam podle zadaného názvu.
        back(): Zavře okno pro odstranění deníkového záznamu.
    """

    def __init__(self, root, diary):
        """
        Inicializuje novou instanci třídy DiaryDeleteUI.

        Args:
            root: Hlavní okno aplikace.
            diary: Instance třídy Diary pro manipulaci s deníkovými záznamy.
        """
        self.diary = diary
        self.root = root
        self.root.title("Odebrat deník")

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
        Odstraní deníkový záznam podle zadaného názvu.
        """
        title = self.entry_title.get()

        self.diary.delete_from_diary(title)

        messagebox.showinfo("Úspěch", "Úspěšně odebráno.")

    def back(self):
        """
        Zavře okno pro odstranění deníkového záznamu.
        """
        self.root.destroy()
