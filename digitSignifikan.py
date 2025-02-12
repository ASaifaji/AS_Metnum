#Kamus
digit_a = 36.45
digit_b = 504
digit_c = 40.05
digit_d = 0.0045
digit_e = 45.0
digit_f = 4500

# Fungsi Mencari n digit signifikan
def digitSignifikan(digit):
    n_digit = 0
    
    # Untuk kasus dimana terdapat titik desimal misal 24.5
    if isinstance(digit, float):
        
        list_digit = list(str(digit)) # Mengubah bilangan misal 24.58 menjadi tupple ['2','4','.', '5','8'] (Memisahkan menjadi digit-digit)
        n = len(list_digit) # Memberikan panjang digit-digit termasuk titik desimalnya
        i = 0 # Selektor tupple 
        j = n - 1 # Selektor tupple
        
        hitung = False # Variabel inisiasi perhitungan
        
        #Loop untuk menghitung digit signifikan di sebelah kiri titik desimal, apabila tidak ada digit signifikan maka tidak akan ada inisiasi perhitungan
        while list_digit[i] != '.':
            
            # Menghitung digit signifikan apabila semua nilai nol di sebelah kiri nilai non-nol telah di lewatkan
            if hitung == True:
                n_digit = n_digit + 1
                i = i + 1
            
            # Apabila masih terdapat nilai '0' di sebelah kiri nilai non-nol
            else:
                
                # Melewati atau menskip semua nilai nol yang berada di kiri nilai non-nol
                if list_digit[i] == '0':
                    i = i + 1
                
                # Apabila selektor tupple membaca nilai non-nol, berarti semua nilai nol di sebelah kiri sudah terlewat dan dapat memulai inisiasi perhitungan
                else :
                    hitung = True

        # reset selektor
        i = 0 # Selektor tupple
        j = n - 1 # Selektor tupple
        
        #Apabila terdapat digit signifikan di sebelah kiri titik desimal berarti seluruh digit di sebelah kanan digit desimal merupakan digit signifikan
        if hitung == True :
            while list_digit[j] != '.' :
                n_digit = n_digit + 1
                j = j - 1
        
        # Apabila tidak terdapat digit signifikan di sebelah kiri desimal (inisiasi perhitungan digit tidak dimulai {hitung = False})
        # Berarti digit nol di kiri dan kanan digit non-nol kecuali diantara digit non-nol bukan merupakan digit signifikan
        else :
            n_takpenting = 0 # banyak digit bukan signifikan
            
            
            # Menghitung digit bukan signifikan di sebelah kiri digit non-nol
            while list_digit[j] == '0':
                n_takpenting = n_takpenting + 1
                j = j - 1
            
            # Menghitung digit bukan signifikan di sebelah kanan digit non-nol
            while list_digit[i] == '0' or list_digit[i] =='.':
                n_takpenting = n_takpenting + 1
                i = i + 1
            
            # Memperoleh digit signifikan dengan eliminasi digit bukan signifikan dari panjang digit
            n_digit = n - n_takpenting
    
    # Untuk Kasus dimana digit bukan desimal / bilangan bulat (20, 30, 14)      
    else :
        if isinstance(digit, int):
            list_digit = list(str(digit)) # Mengubah bilangan misal 24.58 menjadi tupple ['2','4','.', '5','8'] (Memisahkan menjadi digit-digit)
            n = len(list_digit) # Memberikan panjang digit-digit termasuk titik desimalnya
            i = 0 # Selektor tupple 
            j = n - 1 # Selektor tupple
            n_takpenting = 0 # banyaknya digit bukan signifikan
            
            # Menghitung digit bukan signifikan ('0') di sebelah kiri digit non-nol
            while list_digit[i] == '0':
                n_takpenting = n_takpenting + 1
                i = i + 1
            
            # Menghitung digit bukan signifikan ('0') di sebelah kanan digit non-nol
            while list_digit[j] == '0':
                j = j - 1
                n_takpenting = n_takpenting + 1
            
            # memperoleh digit signifikan pada kasus bilangan bulat dengan eliminasi digit bukan signifikan dari panjang digit
            n_digit = n - n_takpenting
        
        # Error Handler apabila salah meginput data
        else:
            n_digit = "[Kesalahan input tipe data, pastikan integer atau float]"
    
    # Mengembalikan nilai berupa banyaknya digit signifikan
    return n_digit

# Output
print(f"{digit_a} mempunyai {digitSignifikan(digit_a)} Digit Signifikan")
print(f"{digit_b} mempunyai {digitSignifikan(digit_b)} Digit Signifikan")
print(f"{digit_c} mempunyai {digitSignifikan(digit_c)} Digit Signifikan")
print(f"{digit_d} mempunyai {digitSignifikan(digit_d)} Digit Signifikan")
print(f"{digit_e} mempunyai {digitSignifikan(digit_e)} Digit Signifikan")
print(f"{digit_f} mempunyai {digitSignifikan(digit_f)} Digit Signifikan")