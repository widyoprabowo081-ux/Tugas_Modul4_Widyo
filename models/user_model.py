import mysql.connector
import hashlib

class UserModel:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="perpustakaan"
            )
            self.cursor = self.db.cursor(dictionary=True)
        except mysql.connector.Error as err:
            self.db = None
            self.cursor = None
            print(f"Error Koneksi Database: {err}")

    @staticmethod
    def hash_password(password):
        # Metode statis untuk pengujian unit hashing SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def autentikasi(self, username, password):
        try:
            hashed_password = self.hash_password(password)
            query = "SELECT * FROM users WHERE username = %s AND password = %s"

            # Mendukung cursor asli maupun mock dari unit test (model.conn)
            cursor = getattr(self, 'cursor', None)
            if not cursor and hasattr(self, 'conn') and self.conn:
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

            cursor = getattr(self, 'cursor', None)
            if not cursor and hasattr(self, 'conn') and self.conn:
                cursor = self.conn.cursor(dictionary=True)

            if not cursor:
                return False

            cursor.execute(query, values)

            if hasattr(self, 'db') and self.db:
                self.db.commit()
            elif hasattr(self, 'conn') and self.conn:
                self.conn.commit()

            return True
        except Exception as err:
            print(f"Error Registrasi: {err}")
            return False