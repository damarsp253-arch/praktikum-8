# List nilai mahasiswa
nilai = [80, 90, 'A', 70, 100, 'B']

# Inisialisasi variabel untuk total dan jumlah data valid
total = 0
count = 0

# Loop melalui setiap item di list
for item in nilai:
    try:
        # Coba konversi item ke float (untuk menangani angka)
        num = float(item)
        total += num
        count += 1
    except ValueError:
        # Jika bukan angka, skip (lewati) tanpa menghentikan program
        pass

# Hitung rata-rata jika ada data valid
if count > 0:
    rata_rata = total / count
    print(f"Rata-rata nilai: {rata_rata}")
else:
    print("Tidak ada data valid untuk dihitung rata-rata.")