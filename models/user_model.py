import hashlib

from config.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "petugas"

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def autentikasi(self, username, password):
        if not self.conn:
            return None

        cursor = self.conn.cursor(dictionary=True)
        query = (
            f"SELECT id_user, username, role FROM {self.table_name} "
            "WHERE username = %s AND password = %s"
        )
        cursor.execute(query, (username, self.hash_password(password)))
        result = cursor.fetchone()
        cursor.close()
        return result
