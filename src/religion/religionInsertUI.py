import tkinter
from tkinter import messagebox


class ReligionInsertUI:
    def __init__(self, root, religion):
        self.religion = religion
        self.root = root
        self.root.title("Přidat náboženský text")

        self.label_title = tkinter.Label(root, text="Název:")
        self.label_title.grid(row=0, column=0, padx=10, pady=5, sticky='we')
        self.entry_title = tkinter.Entry(root)
        self.entry_title.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        self.label_author = tkinter.Label(root, text="Autor:")
        self.label_author.grid(row=3, column=0, padx=10, pady=5, sticky='we')
        self.entry_author = tkinter.Entry(root)
        self.entry_author.grid(row=3, column=1, padx=10, pady=5, sticky='we')

        self.label_publication_date = tkinter.Label(root, text="Datum vydání (RRRR-MM-DD):")
        self.label_publication_date.grid(row=1, column=0, padx=10, pady=5, sticky='we')
        self.entry_publication_date = tkinter.Entry(root)
        self.entry_publication_date.grid(row=1, column=1, padx=10, pady=5, sticky='we')

        self.label_description = tkinter.Label(root, text="Popis:")
        self.label_description.grid(row=2, column=0, padx=10, pady=5, sticky='we')
        self.entry_description = tkinter.Entry(root)
        self.entry_description.grid(row=2, column=1, padx=10, pady=5, sticky='we')

        self.label_language = tkinter.Label(root, text="Jazyk:")
        self.label_language.grid(row=4, column=0, padx=10, pady=5, sticky='we')
        self.entry_language = tkinter.Entry(root)
        self.entry_language.grid(row=4, column=1, padx=10, pady=5, sticky='we')

        self.button_insert = tkinter.Button(root, text="Vložit", command=self.insert)
        self.button_insert.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10, sticky='we')

        root.columnconfigure(1, weight=1)
        for i in range(5):
            root.rowconfigure(i, weight=1)

    def insert(self):
        title = self.entry_title.get()
        publication_date = self.entry_publication_date.get()
        genre = self.entry_description.get()
        author = self.entry_author.get()
        language = self.entry_language.get()

        self.religion.insert_into_religion(title, author, publication_date, genre, language)

        messagebox.showinfo("Úspěch", "Úspěšně přidáno.")

    def back(self):
        self.root.destroy()
