import tkinter.messagebox as messagebox

from Views.anggota_view import AnggotaView
from models.anggota_model import AnggotaModel


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        for anggota in self.model.get_all_anggota():
            self.view.tabel.insert(
                "",
                "end",
                values=(anggota["id_anggota"], anggota["nama"], anggota["alamat"]),
            )

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_anggota(nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data anggota.")

    def perbarui_data(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning(
                "Peringatan", "Pilih data di tabel yang ingin diperbarui terlebih dahulu!"
            )
            return

        id_anggota = self.view.tabel.item(selected_item[0], "values")[0]
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Isi perubahan data di form terlebih dahulu!")
            return

        if self.model.update_anggota(id_anggota, nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data anggota.")

    def hapus_data(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning(
                "Peringatan", "Pilih data di tabel yang ingin dihapus terlebih dahulu!"
            )
            return

        id_anggota = self.view.tabel.item(selected_item[0], "values")[0]
        if not messagebox.askyesno(
            "Konfirmasi", "Apakah Anda yakin ingin menghapus data anggota ini?"
        ):
            return

        if self.model.delete_anggota(id_anggota):
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data anggota.")

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")

    def run(self):
        self.view.mainloop()
