#Widyo Prabowo F5212520068
import tkinter.messagebox as messagebox
from models.buku_models import BukuModel
from Views.buku_view import BukuView

class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        
        # --- TAMBAHAN TUGAS 1: Binding tombol Hapus dan Perbarui ---
        # Pastikan nama tombol di file buku_view.py adalah btn_hapus dan btn_perbarui
        if hasattr(self.view, 'btn_hapus'):
            self.view.btn_hapus.configure(command=self.hapus_data)
        if hasattr(self.view, 'btn_perbarui'):
            self.view.btn_perbarui.configure(command=self.perbarui_data)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (Database)
        data_buku = self.model.get_all_buku()

        # Memasukkan data baru ke dalam tabel View
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def simpan_data(self):
        # Mengambil teks dari input di View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    # --- TAMBAHAN TUGAS 1: Fungsi Hapus Data ---
    def hapus_data(self):
        # Mengambil item/baris yang dipilih pengguna di tabel GUI
        selected_item = self.view.tabel.selection()
        
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin dihapus terlebih dahulu!")
            return
            
        # Mengambil id_buku dari baris yang dipilih (id_buku ada di indeks 0)
        item_values = self.view.tabel.item(selected_item[0], "values")
        id_buku = item_values[0]
        
        # Konfirmasi penghapusan
        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data buku ini?")
        if konfirmasi:
            # Pastikan fungsi delete_buku sudah kamu buat di file buku_model.py
            berhasil = self.model.delete_buku(id_buku) 
            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    # --- TAMBAHAN TUGAS 1: Fungsi Perbarui Data ---
    def perbarui_data(self):
        # Mengambil item/baris yang dipilih pengguna di tabel GUI
        selected_item = self.view.tabel.selection()
        
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin diperbarui terlebih dahulu!")
            return
            
        # Mengambil id_buku dari baris yang dipilih
        item_values = self.view.tabel.item(selected_item[0], "values")
        id_buku = item_values[0]
        
        # Mengambil teks dari input form
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Pilih data di tabel, lalu isi perubahan di form!")
            return

        # Pastikan fungsi update_buku sudah kamu buat di file buku_model.py
        berhasil = self.model.update_buku(id_buku, judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    # Fungsi bantuan untuk membersihkan form inputan
    def bersihkan_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def run(self):
        self.view.mainloop() # Tanda titik (.) dihilangkan di sini