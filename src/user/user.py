from tkinter import messagebox

from src.log_editor.log_editor import Log_editor


class User:
    def __init__(self, db_operator):
        self.log_editor = Log_editor()
        self.connection = db_operator.get_connection()
        self.cursor = db_operator.get_cursor()

    def insert_into_user(self, username, password):
        str_username = str(username)
        str_password = str(password)
        self.cursor.execute(f"INSERT INTO user(username, password) VALUES "
                            f"('{str_username}', '{str_password}')")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně přidán do databáze.")

    def delete_from_user(self, username):
        str_username = str(username)
        self.cursor.execute(f"SELECT * FROM user WHERE username = '{str_username}'")
        output = self.cursor.fetchone()

        if output is None:
            messagebox.showerror("Chyba", "Uživatel nebyl nalezen.")

        self.cursor.execute(f"DELETE FROM user WHERE username = '{str_username}'")
        self.connection.commit()

        self.log_editor.log_debug("Záznam úspěšně odebrán z databáze.")

    def update_user(self, id, username, password, admin):
        int_id = int(id)
        str_username = str(username)
        str_password = str(password)
        int_admin = int(admin)

        self.cursor.execute(f"UPDATE user SET username = '{str_username}',"
                            f" password = '{str_password}', admin = '{int_admin}' WHERE id = {int_id}")
        self.connection.commit()

    def select_from_user_by_username(self, username):
        str_username = str(username)
        self.cursor.execute(f"SELECT * FROM user WHERE username = '{str_username}'")
        return self.cursor.fetchall()

    def select_from_user_by_username_and_pasword(self, username, password):
        str_username = str(username)
        str_password = str(password)
        self.cursor.execute(f"SELECT admin FROM user WHERE username = '{str_username}' AND password = '{str_password}'")
        return self.cursor.fetchone()
