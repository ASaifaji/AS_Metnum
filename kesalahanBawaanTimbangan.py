# Data Objek
objek1 = ['Bola', 0.45]
objek2 = ['Galon', 19]

# Fungsi Sebuah Timbangan
def beratTimbangan(benda) :
    
    berat = 1 # Kesalahan bawaan pada timbangan pengukuran awal seharusnya 0
    
    # Rumus Timbangan, mengambil value berat dari tipe data objek kemudian dimasukkan ke berat
    berat = berat + benda[1]
    
    # Mengembalikan nilai berat
    return berat

# Fungsi Menghitung Kesalahan Bawaan
def kesalahanBawaan(benda) :

    # Menghitung kesalahan bawaan dari pengukuran
    kesalahanBawaan = beratTimbangan(benda) - benda[1]

    # Mengembalikan nilai Kesalahan Bawaan
    return kesalahanBawaan

# Menampilkan Hasil Timbangan dan hasil kesalahaan bawaan
print(f"Berat {objek1[0]} pada timbangan adalah {beratTimbangan(objek1)} kg, Berat sebenarnya {objek1[1]} kg, Kesalahan Bawaanya {kesalahanBawaan(objek1)} kg")
print(f"Berat {objek2[0]} pada timbangan adalah {beratTimbangan(objek2)} kg, Berat sebenarnya {objek2[1]} kg, Kesalahan Bawaanya {kesalahanBawaan(objek2)} kg")