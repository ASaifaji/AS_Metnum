import math

#   Fungsi dari f(x)
def f(x):
    return(x * math.exp(-x) + 1)


#   Metode Regula Falsi
#   a : batas bawah
#   b : batas atas
def regFal(a, b, tol=1e-7, N=100):
    
    iter = 1                                    #   Inisialisasi penghitungan iterasi
    fa = f(a)                                   #   Menghitung nilai f(a) kemudian di simpan di variabel fa
    fb = f(b)                                   #   Menghitung nilai f(b) kemudian di simpan di variabel fb
    x = ((fb * a) - (fa * b)) /(fb - fa)        #   Rumus titik pendekatan x, untuk metode regula falsi
    fx = f(x)                                   #   Menghitung f(x)
    
    #   Inisiasi iterasi
    #   Ketika nilai f(x) dibawah nilai toleransi 1e-7(0,0000001), iterasi dihentikan karena titik sudah sangat mendekati sb x atau f(x) = 0 (berada pada sumbu x)
    while(abs(f(x)) > tol):
        
        iter = iter + 1                         #   Menghitung iterasi
        
        #   Jika iterasi melebihi batas akan di hentikan
        if (iter > N):
            print("iteration maximum exceeded")
            break
        
        #   Apabila f(a).f(x) > 0 (positif), maka batas bawah di iterasi selanjutnya menjadi x
        if ((fa * fx) > 0):
            a = x                               #   x menjadi batas bawah (a)
            fa = fx                             #   karena x menjadi a maka f(x) menjadi f(a)
        
        #   Apabila f(a).f(x) <= 0, maka x menjadi batas atas di iterasi selanjutnya
        else :
            b = x                               #   x menjadi batas atas (b)
            fb = fx                             #   karena x menjadi b maka f(x) menjadi f(b)
        
        x = ((fb * a) - (fa * b)) /(fb - fa)    #   Rumus titik pendekatan x, untuk metode regula falsi
        fx = f(x)                               #   Menghitung f(x)
    
    #   Akar x yang mana f(x) berpotongan pada sb x di x
    akar = x
    
    #   Mengembalikan hasil dalam bentuk sebuah array of string untuk mempermudah pembacaan
    li = ["function f(x) = x * e^-x + 1", f"akar = {akar}", f"iterasi = {iter}"]
    return(li)

#   Realisasi (a = -1, b = 0)
lis = regFal(-1, 0)
for x in lis:
    print(x)