import tkinter
from src.book.bookCommandsUI import BookCommandsUI
from src.charter.charterCommandsUI import CharterCommandsUI
from src.chronicle.chronicleCommandsUI import ChronicleCommandsUI
from src.letter.letterCommandsUI import LetterCommandsUI
from src.religion.religionCommandsUI import ReligionCommandsUI
from src.speech.speechCommandsUI import SpeechCommandsUI
from src.travel_diaries.diaryCommandsUI import DiaryCommandsUI


class UserInterface:
    """
    Třída UserInterface poskytuje uživatelské rozhraní pro výběr typu záznamu
    a spuštění příslušného uživatelského rozhraní pro daný typ záznamu.
    """
    def __init__(self, root, db_operator, admin, user):
        """
        Inicializační metoda třídy UserInterface.

        :param:
            root (tkinter.Tk): Hlavní okno Tkinteru.
            db_operator (DatabaseOperator): Objekt pro operace s databází.
            admin (bool): Příznak, zda je uživatel administrátor.
            user (User): Objekt uživatele pro autentizaci a autorizaci.
        """
        self.db_operator = db_operator
        self.root = root
        self.admin = admin
        self.user = user
        self.root.title("Archiv")

        # Label pro výběr typu záznamu
        self.label_choose_table = tkinter.Label(root, text="Vyberte typ záznamu:")
        self.label_choose_table.grid(row=0, column=0, padx=10, pady=5, sticky='we')

        # Dropdown menu pro výběr typu záznamu
        self.table_var = tkinter.StringVar(root)
        self.table_var.set("Listiny")
        self.table_options = ["Listiny", "Knihy", "Kroniky", "Dopisy", "Náboženské texty", "Projevy a manifesty", "Cestovní deníky"]
        self.table_dropdown = tkinter.OptionMenu(root, self.table_var, *self.table_options)
        self.table_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        # Tlačítko pro výběr záznamu
        self.button_select = tkinter.Button(root, text="Vybrat", command=self.select_table)
        self.button_select.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        # Tlačítko pro ukončení aplikace
        self.button_quit = tkinter.Button(root, text="Ukončit", command=self.quit)
        self.button_quit.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        # Nastavení vahy sloupců a řádků pro automatické přizpůsobení velikosti okna
        root.columnconfigure(1, weight=1)
        for i in range(3):
            root.rowconfigure(i, weight=1)

    def select_table(self):
        """
        Metoda pro zpracování výběru typu záznamu a spuštění příslušného uživatelského rozhraní.
        """
        selected_table = self.table_var.get()
        if selected_table == "Listiny":
            charter_root = tkinter.Tk()
            CharterCommandsUI(charter_root, self.db_operator, self.admin)
            charter_root.mainloop()
        if selected_table == "Knihy":
            book_root = tkinter.Tk()
            BookCommandsUI(book_root, self.db_operator, self.admin)
            book_root.mainloop()
        if selected_table == "Kroniky":
            chronicle_root = tkinter.Tk()
            ChronicleCommandsUI(chronicle_root, self.db_operator, self.admin)
            chronicle_root.mainloop()
        if selected_table == "Náboženské texty":
            religion_root = tkinter.Tk()
            ReligionCommandsUI(religion_root, self.db_operator, self.admin)
            religion_root.mainloop()
        if selected_table == "Dopisy":
            letter_root = tkinter.Tk()
            LetterCommandsUI(letter_root, self.db_operator, self.admin)
            letter_root.mainloop()
        if selected_table == "Projevy a manifesty":
            speech_root = tkinter.Tk()
            SpeechCommandsUI(speech_root, self.db_operator, self.admin)
            speech_root.mainloop()
        if selected_table == "Cestovní deníky":
            diary_root = tkinter.Tk()
            DiaryCommandsUI(diary_root, self.db_operator, self.admin)
            diary_root.mainloop()

    def quit(self):
        """
        Metoda pro ukončení aplikace.
        """
        self.root.quit()
