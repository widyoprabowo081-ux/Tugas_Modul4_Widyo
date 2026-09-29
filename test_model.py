from models.buku_models import BukuModel

model = BukuModel()

print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke Laragon MySQL!")

print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] {buku['judul']} - "
        f"{buku['penulis']} ({buku['tahun_terbit']})"
    )