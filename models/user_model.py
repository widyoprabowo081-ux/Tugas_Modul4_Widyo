import hashlib
from config.database import Database  #[cite: 15]

class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"  #[cite: 15]

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()  #[cite: 15]

    def autentikasi(self, username, password):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            password_hash = self.hash_password(password)  #[cite: 15]
            query = f"SELECT id_user, username, role FROM {self.table_name} WHERE username = %s AND password = %s"  #[cite: 15]
            cursor.execute(query, (username, password_hash))  #[cite: 15]
            user = cursor.fetchone()  #[cite: 15]
            cursor.close()
            return user
        return None  #[cite: 15]

    # Tugas 1: Fungsi Registrasi User Baru dengan Hash SHA-256
    def register_user(self, username, password, role="anggota"):
        if self.conn:
            cursor = self.conn.cursor()
            password_hash = self.hash_password(password)  #[cite: 20]
            query = f"INSERT INTO {self.table_name} (username, password, role) VALUES (%s, %s, %s)"
            try:
                cursor.execute(query, (username, password_hash, role))
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Error Register: {e}")
                cursor.close()
                return False
        return False