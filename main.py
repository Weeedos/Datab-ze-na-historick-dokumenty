import sys
import tkinter
from tkinter import messagebox
from src.log_editor.logeditor import LogEditor
from src.login.loginMenuUI import LoginMenuUI
from src.dbOperator.dbOperator import DatabaseOperator
from src.user.user import User


def main():
    """
    Hlavní funkce pro inicializaci aplikace.

    Tato funkce inicializuje potřebné komponenty aplikace, včetně připojení k databázi,
    mechanismu pro záznam událostí, autentizace uživatele a grafického uživatelského rozhraní.
    """
    try:
        log_editor = LogEditor()

        db_operator = DatabaseOperator()
        db_operator.connect()

        user = User(db_operator)

        root = tkinter.Tk()

        LoginMenuUI(root, db_operator, user, log_editor)

        root.mainloop()

    except Exception as err:
        messagebox.showerror("Chyba", f"Došlo k chybě: {str(err)}")
        log_editor.log_error(f"Chyba: {str(err)}")
    finally:
        db_operator.disconnect()


if __name__ == "__main__":
    main()
