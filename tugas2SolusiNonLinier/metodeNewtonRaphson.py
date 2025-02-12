import math

#   Fungsi dari f(x)
def f(x):
    return(math.exp(x) + 2**(-x) + 2*math.cos(x) - 6)

#   Fungsi f'(x)
def fp(x):
    return(-2*math.sin(x) + math.exp(x) - math.log(2)/(2**x))


#   Metode Newton-Raphson
#   fp : batas bawah
#   x0 : batas atas
def newRaph(x0, tol=1e-5, N=100):
    
    iter = 0                                    #   Inisialisasi penghitungan iterasi
    xlama = x0                                  #   Tebakan x awal ditaruh di x lama
    xbaru = xlama - f(xlama)/fp(xlama)          #   Rumus titik pendekatan Newton-Raph
    
    print(f"{'iterasi':<10}{'xn':<20}{'xn+1':<20}")
    print("==============================================")
    
    #   Jika selisih x baru dan x lama dibawah nilai toleransi, maka f(x) = 0 atau sangat mendekati 0
    while(abs(xbaru - xlama) > tol):
        
        iter = iter + 1                         #   Menghitung iterasi
        
        #   Jika iterasi melebihi batas iterasi, maka tidak ada solusi dan akan dihentikan
        if (iter > N):
            print("no solution found")
            break
        
        print(f"{iter:<10}{'{:.10f}'.format(xlama):<20}{'{:.10f}'.format(xbaru):<20}")
        
        xlama = xbaru                           #   x saat ini menjadi x lama
        xbaru = xlama - f(xlama)/fp(xlama)      #   Rumus titik pendekatan (menghitung x selanjutnya dari x saat ini)
    
    akar = xbaru                                #   akarnya adalah x saat ini
    
    #   Mengembalikan nilai kedalam list of string untuk kemudahan membaca
    li = ["f(x) = e^x + 2^-x + 2cos(x) - 6",f"akar x = {akar}",f"iterasi = {iter}"]
    return li

# Realisasi program dimana newRaph(nilai x sembarang)
lis = newRaph(1)
for x in lis:
    print("================================================")
    print(x)