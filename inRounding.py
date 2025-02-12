# Fungsi Pembulatan dengan menghapus digit tak diinginkan tanpa pertimbangan berikutnya
# Parameter :   bil (float) : bilangan yang akan dipenggal
# Return    :   roundBil : Nilai bilangan yang telah dipotong ke 2 digit
def inRounding (bil) :
    
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
    nInt = j - n                    # panjang digit desimal
    
    # Selama digit terakhir bukan digit ke-3 digit terakhir akan dihapus
    while n > 3:
        
        list_bil = list_bil[:-1]    # Menghapus digit terakhir
        n = n - 1                   # Panjang digit berkurang
        j = j - 1                   # Selektor
    
    temp = list_bil[-1]             # Menyimpan digit terakhir (digit ke-3 desimal) untuk referensi penambahan digit ke-2 desimal
    list_bil = list_bil[:-1]        # Menghapus digit terakhir di list (digit ke-3 desimal)
    
    # digit ke-2 desimal ditambah 1 apabila digit ke-3 lebih dari 5 atau sama dengan 5 dan digit ke-2 ganjil
    if (int(temp)>5):
        if list_bil[-1] == '9':
            list_bil[-2] = str(int(list_bil[-2]) + 1)
            list_bil[-1] = '0'
        else:
            temp = int(list_bil[-1]) + 1
            list_bil[-1] = str(temp)
    else :
        if (int(temp)==5 and int(list_bil[-1]) % 2 == 1) :
            temp = int(list_bil[-1]) + 1
            list_bil[-1] = str(temp)
            
                
    
    # Menggabungkan list of character list_bil menjadi satu string bil
    bil = ""
    for x in list_bil :
        bil = bil+x

    # Mengubah tipe data dari string ke float (opsional) dan mengembalikan nilainy
    roundBil = float(bil)
    return roundBil

# definisi
angka = 4.1264

# Realisasi Output
print(inRounding(angka))