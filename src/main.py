import tkinter
from tkinter import messagebox
from src.log_editor.log_editor import Log_editor
from src.login.loginMenuUI import LoginMenuUI
from src.dbOperator.dbOperator import DatabaseOperator
from src.user.user import User


def main():
    try:
        log_editor = Log_editor()
        db_operator = DatabaseOperator()
        db_operator.connect()
        user = User(db_operator)
        root = tkinter.Tk()
        LoginMenuUI(root, db_operator, user)
        root.mainloop()
    except Exception as err:
        messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
        log_editor.log_error(f"Chyba: {str(err)}")
    finally:
        db_operator.disconnect()


if __name__ == "__main__":
    main()
