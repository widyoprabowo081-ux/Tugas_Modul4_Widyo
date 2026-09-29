print("=== Menu Pengecek Kalori Sederhana ===")
print("1. Nasi Goreng")
print("2. Salad Buah")
print("3. Ayam Geprek")
# Meminta pengguna memilih nomor makanan
pilihan = input("Pilih nomor makanan (1/2/3): ")
# 1. IF-ELSE untuk menentukan makanan dan jumlah kalori
if pilihan == '1':
    makanan = "Nasi Goreng"
    kalori = 450
elif pilihan == '2':
    makanan = "Salad Buah"
    kalori = 150
elif pilihan == '3':
    makanan = "Ayam Geprek"
    kalori = 600
else:
    makanan = "Tidak ada di menu"
    kalori = 0
# 2. Menampilkan hasil dan memberikan komentar dengan IF-ELSE
if kalori > 0:
    print(f"\nAnda memilih: {makanan}")
    print(f"Total Kalori: {kalori} kalori")
    
    # Cek apakah kalorinya tinggi atau rendah
    if kalori > 400:
        print("Pesan: Kalorinya cukup tinggi, jangan lupa banyak minum air dan olahraga ya!")
    else:
        print("Pesan: Kalorinya rendah, sangat aman untuk camilan diet!")
        
else:
    print("\nPilihan salah. Silakan masukkan angka 1, 2, atau 3.")