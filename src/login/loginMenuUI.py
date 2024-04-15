import hashlib
import tkinter
from tkinter import messagebox

from src.userInterface.userInterface import UserInterface


class LoginMenuUI:
    def __init__(self, root, db_operator, user):
        self.root = root
        self.db_operator = db_operator
        self.user = user

        self.label_username = tkinter.Label(root, text="Uživatelské jméno:")
        self.label_username.grid(row=0, column=0, padx=10, pady=5)
        self.entry_username = tkinter.Entry(root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        self.label_password = tkinter.Label(root, text="Heslo:")
        self.label_password.grid(row=1, column=0, padx=10, pady=5)
        self.entry_password = tkinter.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        self.register_button = tkinter.Button(self.root, text="Register", command=self.register)
        self.register_button.grid(row=2, column=1, padx=10, pady=5)

        self.login_button = tkinter.Button(self.root, text="Login", command=self.login)
        self.login_button.grid(row=3, column=1, padx=10, pady=5)

        self.button_quit = tkinter.Button(root, text="Ukončit", command=self.quit)
        self.button_quit.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        admin = self.user.select_from_user_by_username_and_pasword(username, hashed_password)

        if admin is None:
            messagebox.showerror("Chyba", "Nesprávné uživatelské jméno nebo heslo.")
            raise Exception("Nesprávné uživatelské jméno nebo heslo.")

        self.root.destroy()
        root = tkinter.Tk()
        UserInterface(root, self.db_operator, admin, self.user)
        root.mainloop()

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        self.user.insert_into_user(username, hashed_password)

        messagebox.showinfo("Úspěch", "Registrace úspěšná.")

    def quit(self):
        self.root.destroy()