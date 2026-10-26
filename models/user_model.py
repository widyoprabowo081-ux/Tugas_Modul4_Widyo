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

    def autentikasi(self, username, password):
        try:
            hashed_password = self.hash_password(password)
            query = "SELECT * FROM users WHERE username = %s AND password = %s"

            cursor = getattr(self, "cursor", None)
            if not cursor and getattr(self, "conn", None):
                cursor = self.conn.cursor(dictionary=True)

            if not cursor:
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

            cursor = getattr(self, "cursor", None)
            if not cursor and getattr(self, "conn", None):
                cursor = self.conn.cursor(dictionary=True)

            if not cursor:
                return False

            cursor.execute(query, values)

            if getattr(self, "db", None):
                self.db.commit()
            elif getattr(self, "conn", None):
                self.conn.commit()

            return True
        except Exception as err:
            print(f"Error Registrasi: {err}")
            return False
