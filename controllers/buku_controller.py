import tkinter.messagebox as messagebox
from models.buku_models import BukuModel
from Views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()
        
        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")
        
        # ==========================================
        # PENEMPATAN NOMOR 1: Binding Tombol Utama
        # ==========================================
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)
        
        # Binding Tombol Logout (Bagian dari Tugas 3)
        self.view.btn_logout.configure(command=self.proses_logout)
        
        # OTORISASI: Jika bukan admin, nonaktifkan form input dan tombol
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")
            
            # --- JAWABAN TUGAS 2 ---
            # Mengunci tombol Update dan Delete jika pengguna adalah anggota
            self.view.btn_update.configure(state="disabled")
            self.view.btn_delete.configure(state="disabled")
            
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
            
        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def simpan_data(self):
        # Proteksi ganda di level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return
            
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()
        
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
            
        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    # ==========================================
    # PENEMPATAN NOMOR 2: Fungsi Update & Delete
    # ==========================================
    def perbarui_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk mengubah data!")
            return

        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Pilih Data", "Silakan pilih baris data di tabel terlebih dahulu!")
            return

        id_buku = self.view.tabel.item(selected_item)['values'][0]
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi untuk update!")
            return

        if self.model.update_buku(id_buku, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data.")

    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Pilih Data", "Silakan pilih baris data di tabel yang ingin dihapus!")
            return

        id_buku = self.view.tabel.item(selected_item)['values'][0]

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data buku ini?")
        if konfirmasi:
            if self.model.delete_buku(id_buku):
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_tahun.delete(0, 'end')
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data.")

    # --- JAWABAN TUGAS 3 (Fungsi Logout) ---
    def proses_logout(self):
        # 1. Hancurkan/tutup jendela perpustakaan saat ini
        self.view.destroy()
        
        # 2. Panggil kembali jendela Login
        from controllers.auth_controller import AuthController
        app_login = AuthController()
        app_login.run()

    def run(self):
        self.view.mainloop()