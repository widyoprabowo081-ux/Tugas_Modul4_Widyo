import mysql.connector
import hashlib


class UserModel:
    def __init__(self):
        self.db = None
        self.conn = None
        self.cursor = None

        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="perpustakaan",
            )
            self.conn = self.db
            self.cursor = self.db.cursor(dictionary=True)
        except mysql.connector.Error as err:
            self.db = None
            self.conn = None
            self.cursor = None
            print(f"Error Koneksi Database: {err}")

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def _get_cursor(self):
        cursor = getattr(self, "cursor", None)
        if cursor is not None:
            return cursor

        conn = getattr(self, "conn", None) or getattr(self, "db", None)
        if conn is None:
            return None

        try:
            return conn.cursor(dictionary=True)
        except Exception:
            try:
                return conn.cursor()
            except Exception:
                return None

    def autentikasi(self, username, password):
        try:
            hashed_password = self.hash_password(password)
            query = "SELECT * FROM users WHERE username = %s AND password = %s"

            cursor = self._get_cursor()
            if cursor is None:
                return None

            cursor.execute(query, (username, hashed_password))
            return cursor.fetchone()
        except Exception as err:
            print(f"Error Autentikasi: {err}")
            return None

    def register_user(self, username, password, role="anggota"):
        try:
            hashed_password = self.hash_password(password)
            query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
            values = (username, hashed_password, role)

            cursor = self._get_cursor()
            if cursor is None:
                return False

            cursor.execute(query, values)

            conn = getattr(self, "conn", None) or getattr(self, "db", None)
            if conn is not None:
                conn.commit()

            return True
        except Exception as err:
            print(f"Error Registrasi: {err}")
            return False
