import tkinter.messagebox as messagebox
from models.buku_models import BukuModel
from Views.buku_view import BukuView

class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Binding tombol-tombol yang ada di View
        if hasattr(self.view, 'btn_simpan'):
            self.view.btn_simpan.configure(command=self.simpan_data)
        
        # Binding tombol Hapus dan Perbarui
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.btn_update.configure(command=self.perbarui_data)

        # Memuat data ke tabel saat aplikasi pertama kali dijalankan
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Membersihkan data tabel di tampilan saat ini
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari database melalui model
        data_buku = self.model.get_all_buku()

        # Memasukkan data ke dalam tabel view
        for buku in data_buku:
            # Menggunakan struktur dictionary dari hasil fetch MySQL
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def simpan_data(self):
        # Mengambil nilai dari form input
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi form kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Mengirim data ke model untuk disimpan
        berhasil = self.model.create_buku(judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data buku.")

    def hapus_data(self):
        # Mengambil baris tabel yang diklik pengguna
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin dihapus terlebih dahulu!")
            return
            
        # Mengambil id_buku dari baris yang dipilih (indeks 0)
        id_buku = self.view.tabel.item(selected_item[0], "values")[0]
        
        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data buku ini?")
        if konfirmasi:
            berhasil = self.model.delete_buku(id_buku) 
            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def perbarui_data(self):
        # Mengambil baris tabel yang diklik pengguna
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin diperbarui terlebih dahulu!")
            return
            
        # Mengambil id_buku dari baris yang dipilih (indeks 0)
        id_buku = self.view.tabel.item(selected_item[0], "values")[0]
        
        # Mengambil nilai baru dari form input
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Isi perubahan data di form terlebih dahulu!")
            return

        # Mengirim data pembaruan ke model
        berhasil = self.model.update_buku(id_buku, judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def bersihkan_form(self):
        # Mengosongkan form input setelah aksi selesai
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def run(self):
        # Menjalankan mainloop aplikasi GUI
        self.view.mainloop()