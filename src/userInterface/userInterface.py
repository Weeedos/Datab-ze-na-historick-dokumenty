import tkinter
from src.book.bookCommandsUI import BookCommandsUI
from src.charter.charterCommandsUI import CharterCommandsUI
from src.chronicle.chronicleCommandsUI import ChronicleCommandsUI
from src.letter.letterCommandsUI import LetterCommandsUI
from src.religion.religionCommandsUI import ReligionCommandsUI
from src.speech.speechCommandsUI import SpeechCommandsUI
from src.travel_diaries.diaryCommandsUI import DiaryCommandsUI


class UserInterface:
    def __init__(self, root, db_operator):
        self.db_operator = db_operator
        self.root = root
        self.root.title("Archiv")

        self.label_choose_table = tkinter.Label(root, text="Vyberte typ záznamu:")
        self.label_choose_table.grid(row=0, column=0, padx=10, pady=5)

        self.table_var = tkinter.StringVar(root)
        self.table_var.set("Listiny")

        self.table_options = ["Listiny", "Knihy", "Kroniky", "Dopisy", "Náboženské texty", "Projevy a manifesty", "Cestovní deníky"]
        self.table_dropdown = tkinter.OptionMenu(root, self.table_var, *self.table_options)
        self.table_dropdown.grid(row=0, column=1, padx=10, pady=5)

        self.button_select = tkinter.Button(root, text="Vybrat", command=self.select_table)
        self.button_select.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.button_quit = tkinter.Button(root, text="Ukončit", command=self.quit)
        self.button_quit.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def select_table(self):
        selected_table = self.table_var.get()
        if selected_table == "Listiny":
            charter_root = tkinter.Tk()
            CharterCommandsUI(charter_root, self.db_operator)
            charter_root.mainloop()
        if selected_table == "Knihy":
            book_root = tkinter.Tk()
            BookCommandsUI(book_root, self.db_operator)
            book_root.mainloop()
        if selected_table == "Kroniky":
            chronicle_root = tkinter.Tk()
            ChronicleCommandsUI(chronicle_root, self.db_operator)
            chronicle_root.mainloop()
        if selected_table == "Náboženské texty":
            religion_root = tkinter.Tk()
            ReligionCommandsUI(religion_root, self.db_operator)
            religion_root.mainloop()
        if selected_table == "Dopisy":
            letter_root = tkinter.Tk()
            LetterCommandsUI(letter_root, self.db_operator)
            letter_root.mainloop()
        if selected_table == "Projevy a manifesty":
            speech_root = tkinter.Tk()
            SpeechCommandsUI(speech_root, self.db_operator)
            speech_root.mainloop()
        if selected_table == "Cestovní deníky":
            diary_root = tkinter.Tk()
            DiaryCommandsUI(diary_root, self.db_operator)
            diary_root.mainloop()

    def quit(self):
        self.root.quit()
