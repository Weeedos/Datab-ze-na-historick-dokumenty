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
        # Inicializace LogEditoru pro zaznamenávání událostí aplikace
        log_editor = LogEditor()

        # Inicializace DatabaseOperatoru pro operace s databází
        db_operator = DatabaseOperator()
        db_operator.connect()  # Připojení k databázi

        # Inicializace objektu User pro správu uživatelů
        user = User(db_operator)

        # Vytvoření hlavního okna Tkinteru
        root = tkinter.Tk()

        # Inicializace grafického uživatelského rozhraní pro přihlašovací menu s potřebnými komponentami
        LoginMenuUI(root, db_operator, user, log_editor)

        # Spuštění smyčky událostí Tkinteru
        root.mainloop()

    except Exception as err:
        # Pokud dojde k chybě, zobrazí se dialogové okno s chybovou zprávou a chyba se zaloguje
        messagebox.showerror("Chyba", f"Došlo k chybě: {str(err)}")
        log_editor.log_error(f"Chyba: {str(err)}")

    finally:
        # Ujistěte se, že je uzavřeno připojení k databázi
        db_operator.disconnect()


if __name__ == "__main__":
    main()
