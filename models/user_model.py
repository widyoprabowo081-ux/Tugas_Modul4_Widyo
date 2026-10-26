import mysql.connector
import hashlib

class UserModel:
    def __init__(self):
        # Konfigurasi koneksi ke database MySQL
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Biarkan kosong jika default Laragon
                database="perpustakaan"
            )
            self.cursor = self.db.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Error Koneksi Database: {err}")

    def autentikasi(self, username, password):
        try:
            # Mengubah teks sandi yang diketik saat login menjadi hash SHA-256
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            # Mencocokkan data di database
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, hashed_password))
            
            # Mengembalikan data pengguna jika cocok, atau None jika gagal
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error Autentikasi: {err}")
            return None

    def register_user(self, username, password, role="anggota"):
        try:
            # Mengubah teks password baru menjadi hash SHA-256
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            # Menyimpan data pengguna baru ke database
            query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
            values = (username, hashed_password, role)
            
            self.cursor.execute(query, values)
            self.db.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error Registrasi: {err}")
            return False