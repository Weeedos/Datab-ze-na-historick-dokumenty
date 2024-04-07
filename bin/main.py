import tkinter
from tkinter import messagebox
from src.userInterface.userInterface import UserInterface
from src.dbOperator.dbOperator import DatabaseOperator


def main():
    try:
        db_operator = DatabaseOperator()
        db_operator.connect()
        root = tkinter.Tk()
        UserInterface(root, db_operator)
        root.mainloop()
    except Exception as err:
        messagebox.showerror("Chyba", f"Nastala chyba: {str(err)}")
    finally:
        db_operator.disconnect()


if __name__ == "__main__":
    main()
