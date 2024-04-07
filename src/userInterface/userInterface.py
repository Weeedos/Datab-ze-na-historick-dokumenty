import tkinter
from src.charter.charterCommandsUI import CharterCommandsUI


class UserInterface:
    def __init__(self, root, db_operator):
        self.db_operator = db_operator
        self.root = root
        self.root.title("Archiv")

        self.label_choose_table = tkinter.Label(root, text="Vyberte typ záznamu:")
        self.label_choose_table.grid(row=0, column=0, padx=10, pady=5)

        self.table_var = tkinter.StringVar(root)
        self.table_var.set("listiny")

        self.table_options = ["listiny"]
        self.table_dropdown = tkinter.OptionMenu(root, self.table_var, *self.table_options)
        self.table_dropdown.grid(row=0, column=1, padx=10, pady=5)

        self.button_select = tkinter.Button(root, text="Vybrat", command=self.select_table)
        self.button_select.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.button_quit = tkinter.Button(root, text="Ukončit", command=self.quit)
        self.button_quit.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def select_table(self):
        selected_table = self.table_var.get()
        if selected_table == "listiny":
            charter_root = tkinter.Tk()
            CharterCommandsUI(charter_root, self.db_operator)
            charter_root.mainloop()

    def quit(self):
        self.root.quit()
