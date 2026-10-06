from models.anggota_model import AnggotaModel
from models.buku_models import BukuModel


def uji_buku():
    model = BukuModel()
    if not model.conn:
        print("Database tidak terhubung. Pastikan MySQL Laragon sudah aktif.")
        return

    print("=== Uji Create Buku ===")
    if model.create_buku("Buku Uji CRUD", "Penulis Uji", 2024):
        print("Buku berhasil ditambahkan.")
    else:
        print("Buku gagal ditambahkan.")

    print("\n=== Daftar Buku ===")
    daftar_buku = model.get_all_buku()
    for buku in daftar_buku:
        print(
            f"[{buku['id_buku']}] {buku['judul']} - "
            f"{buku['penulis']} ({buku['tahun_terbit']})"
        )

    try:
        id_buku = int(input("\nMasukkan id_buku untuk diuji: "))
    except ValueError:
        print("ID buku harus berupa angka.")
        return

    print("\n=== Uji Update Buku ===")
    berhasil_update = model.update_buku(
        id_buku,
        "Judul Setelah Update",
        "Penulis Uji",
        2025,
    )
    buku_setelah_update = next(
        (buku for buku in model.get_all_buku() if buku["id_buku"] == id_buku),
        None,
    )
    if (
        berhasil_update
        and buku_setelah_update
        and buku_setelah_update["judul"] == "Judul Setelah Update"
        and buku_setelah_update["penulis"] == "Penulis Uji"
        and buku_setelah_update["tahun_terbit"] == 2025
    ):
        print("Data buku berhasil diperbarui.")
    else:
        print("Buku tidak ditemukan atau gagal diperbarui.")

    print("\n=== Uji Delete Buku ===")
    konfirmasi = input(
        f"Yakin menghapus buku dengan id {id_buku}? (y/t): "
    ).lower()
    if konfirmasi == "y":
        berhasil_hapus = model.delete_buku(id_buku)
        masih_ada = any(
            buku["id_buku"] == id_buku for buku in model.get_all_buku()
        )
        if berhasil_hapus and not masih_ada:
            print("Data buku berhasil dihapus.")
        else:
            print("Buku tidak ditemukan atau gagal dihapus.")
    else:
        print("Penghapusan dibatalkan.")


def uji_anggota():
    model = AnggotaModel()
    if not model.conn:
        print("Database tidak terhubung. Pastikan MySQL Laragon sudah aktif.")
        return

    print("\n=== Uji Create Anggota ===")
    nama = input("Masukkan nama anggota: ")
    alamat = input("Masukkan alamat anggota: ")
    if model.create_anggota(nama, alamat):
        print("Anggota berhasil ditambahkan.")
    else:
        print("Anggota gagal ditambahkan.")

    print("\n=== Daftar Anggota ===")
    daftar_anggota = model.get_all_anggota()
    for anggota in daftar_anggota:
        print(
            f"[{anggota['id_anggota']}] "
            f"{anggota['nama']} - {anggota['alamat']}"
        )


if __name__ == "__main__":
    uji_buku()
    uji_anggota()