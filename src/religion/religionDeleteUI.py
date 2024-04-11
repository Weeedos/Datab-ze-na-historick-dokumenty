import tkinter
from tkinter import messagebox


class ReligionDeleteUI:
    def __init__(self, root, religion):
        self.religion = religion
        self.root = root
        self.root.title("Odebrat náboženský text")

        self.label_title = tkinter.Label(root, text="Název:")
        self.label_title.grid(row=0, column=0, padx=10, pady=5)
        self.entry_title = tkinter.Entry(root)
        self.entry_title.grid(row=0, column=1, padx=10, pady=5)

        self.button_delete = tkinter.Button(root, text="Odebrat", command=self.delete)
        self.button_delete.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.button_back = tkinter.Button(root, text="Zpátky", command=self.back)
        self.button_back.grid(row=6, column=2, padx=10, pady=10)

    def delete(self):
        title = self.entry_title.get()

        self.religion.delete_from_religion(title)

        messagebox.showinfo("Úspěch", "Úspěšně odebráno.")

    def back(self):
        self.root.destroy()