from models.user_model import UserModel

# Menginisialisasi objek UserModel
model = UserModel()

# Menguji eksekusi metode register_user
berhasil = model.register_user("dosenbaru", "rahasia123", "admin")

if berhasil:
    print("Berhasil! Silakan cek tabel users di database.")
else:
    print("Gagal menyimpan data.")