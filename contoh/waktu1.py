# contoh program menghitung selisih waktu

from datetime import datetime

# catat waktu mulai
awal = datetime.now()

nama_depan = input("Nama Depan?")
nama_belakang = input("Nama Belakang?")

# catat waktu selesai
akhir = datetime.now()

# hitung selisih waktu
selisih = akhir - awal

# hasil penjumlahan 2 objek datetime akan menghasilkan objek `timedelta`

print("Total waktu Anda menulis:", selisih.total_seconds(),"detik")

