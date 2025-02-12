# Angka Sebenarnya
angkaSebenarnya = 1/6
print(f"Angka Sebenarnya {angkaSebenarnya}...(tak hingga)")

# Angka yang dibulatkan
angkaPembulatan = round(1/6, 6)
print(f"Angka Setelah dibulatkan {angkaPembulatan}")

# Fungsi Galatnya
def kesalahanPembulatan(angkaSebenarnya, angkaPembulatan) :
    galat = angkaSebenarnya - angkaPembulatan
    
    # Menggunakan format 8 digit untuk menghindari notasi sains '3.3e-07'
    galat_8dig = '{:.8f}'.format(galat)
    return galat_8dig

# Mengeluarkan hasil hitung galat
print(f"Galatnya sebesar {kesalahanPembulatan(angkaSebenarnya, angkaPembulatan)}")