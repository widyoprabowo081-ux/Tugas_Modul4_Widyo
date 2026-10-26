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
            # Penanganan agar tidak error saat dijalankan di GitHub Actions tanpa database aktif
            self.db = None
            self.cursor = None
            print(f"Error Koneksi Database: {err}")

    @staticmethod
    def hash_password(password):
        # Metode statis untuk pengujian unit hashing SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def autentikasi(self, username, password):
        if not self.cursor:
            return None
        try:
            hashed_password = self.hash_password(password)
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, hashed_password))
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error Autentikasi: {err}")
            return None

    def register_user(self, username, password, role="anggota"):
        if not self.cursor:
            return False
        try:
            hashed_password = self.hash_password(password)
            query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
            values = (username, hashed_password, role)
            self.cursor.execute(query, values)
            self.db.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error Registrasi: {err}")
            return False