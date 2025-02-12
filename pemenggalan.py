# Fungsi Pembulatan dengan menghapus digit tak diinginkan tanpa pertimbangan berikutnya
# Parameter :   bil (float) : bilangan yang akan dipenggal
# Return    :   chopdBil : Nilai bilangan yang telah dipotong ke 7 digit
def pemenggalan (bil) :
    
    # Mengubah tipe data bil dari float ke list of character agar mudah mengatur digit-digitnya
    list_bil = list(str(bil))
    
    # Panjang digit
    j = len(list_bil) - 1           # Inisialisasi Selektor
    n = 0                           # Inisialisasi panjang digit
    
    # Menghitung panjang digit desimal
    while list_bil[j] != '.':
        j = j - 1                   # Selektor
        n = n + 1                   # Panjang digit + 1

    j = len(list_bil) - 1           # Reset selektor
    
    # Selama digit terakhir bukan digit ke-7 digit terakhir akan dihapus
    while n > 7:
        
        list_bil = list_bil[:-1]    # Menghapus digit terakhir
        n = n - 1                   # Panjang digit berkurang
        j = j - 1                   # Selektor
    
    # Menggabungkan list of character list_bil menjadi satu string bil
    bil = ""
    for x in list_bil :
        bil = bil+x

    # Mengubah tipe data dari string ke float (opsional) dan mengembalikan nilainy
    chopdBil = float(bil)
    return chopdBil
        

# Definisi bilangan
pi = 3.14159265359

# Realisasi Output
print(pemenggalan(pi))