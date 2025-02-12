import math

#   Fungsi dari f(x)
def f(x):
    return(x - math.exp(-x))

#   Fungsi f'(x)
def fp(x):
    return(1 + math.exp(-x))


#   Metode Secant
#   fp : batas bawah
#   x : batas atas
def secant(x, tol=1e-7, N=100):
    
    iter    = 0                                         #   Inisialisasi penghitungan iterasi
    xlama   = x                                         #   Tebakan x awal ditaruh di x lama
    fxlama  = f(x)                                      #   Menghitung fungsi f(x)
    x       = xlama + 10*tol                            #   Titik pendekatan kedua (x saat ini)
    
    #   Jika selisih x dan x lama dibawah nilai toleransi, maka f(x) = 0 atau sangat mendekati 0
    while(abs(x - xlama) > tol):
        
        iter = iter + 1                                 #   Menghitung iterasi
        
        #   Jika iterasi melebihi batas iterasi, maka tidak ada solusi dan akan dihentikan
        if (iter > N):
            print("no solution found")
            break
        
        fx      = f(x)                                  #   Hitung fungsi f(x), x saat ini
        xbaru   = x - fx*((xlama - x)/(fxlama - fx))    #   Rumus pendekatan secant, menghitung x selanjutnya
        xlama   = x                                     #   x saat ini menjadi x lama
        fxlama  = fx                                    #   karena x menjadi x lama, maka f(x) menjadi f(x) lama
        x       = xbaru                                 #   x baru menjadi x saat ini
        
    
    akar = xbaru                                        #   akarnya adalah x saat ini
    
    #   Mengembalikan nilai kedalam list of string untuk kemudahan membaca
    li = ["f(x) = x - e^-x",f"akar x = {akar}",f"iterasi = {iter}"]
    return li

# Realisasi program dimana secant(nilai x sembarang)
lis = secant(0)
for x in lis:
    print(x)