# Widyo Prabowo F5212520068
from unittest.mock import MagicMock
from models.buku_models import BukuModel

# ==========================================================
# 1. Unit Test: Test Tambah Data (Sesuai Prosedur Kerja Poin 5)
# ==========================================================
def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True

    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()

    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()


# ==========================================================
# 2. Unit Test: Test Ambil Semua Data (Sesuai Tugas Poin 3)
# ==========================================================
def test_get_all_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    
    # Data simulasi/dummy yang seolah-olah dikembalikan dari MySQL
    data_dummy = [
        {'id_buku': 1, 'judul': 'Buku Testing', 'penulis': 'Penulis QA', 'tahun_terbit': 2026}
    ]
    mock_cursor.fetchall.return_value = data_dummy
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi get_all_buku
    hasil = model.get_all_buku()

    # Memverifikasi apakah hasil sesuai dengan data dummy
    assert hasil == data_dummy

    # Memverifikasi apakah perintah query dipanggil
    mock_cursor.execute.assert_called_once()