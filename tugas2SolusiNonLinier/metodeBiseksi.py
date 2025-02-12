import math

# Fungsi dari f(x)
def f(x):
    return((math.exp(x)) - (x**2) + (3*x) - 2)


# Metode Biseksi
# a : batas bawah
# b : batas atas
def biseksi(a, b, tol=1e-5, N=100):
    iter = 0                # Inisialisasi penghitungan iterasi
    fa = f(a)               # Menghitung nilai f(a) kemudian di simpan di variabel fa
    fb = f(b)               # Menghitung nilai f(b) kemudian di simpan di variabel fb
    
    print(f"{'iterasi':<10}{'a':<20}{'b':<20}{'x':<20}{'fa':<20}{'fx':<20}")
    print("==========================================================================================================")
    
    # Inisiasi iterasi
    # Ketika selisih batas atas dan bawah sudah dibawah 1e-7(0,0000001) maka iterasi berhenti karena f(x) sudah sangat mendekati sumbu x atau f(x) = 0 (ada pada sumbu x)
    while(abs(b-a) > tol):
        iter = iter + 1     # Menghitung iterasi
        
        # Jika iterasi melebihi batas akan di hentikan
        if (iter > N):
            print("iteration maximum exceeded")
            break
        
        x = (a + b)/2       # Hitung nilai x yang akan diuji dengan mengambil nilai tengah, membelah (biseksi) batas menjadi dua
        fx = f(x)           # Hitung f(x)
        
        print(f"{iter:<10}{'{:.10f}'.format(a):<20}{'{:.10f}'.format(b):<20}{'{:.10f}'.format(x):<20}{'{:.10f}'.format(fa):<20}{'{:.10f}'.format(fx):<20}")
        
        # Apabila f(a).f(x) > 0 (positif), maka batas bawah di iterasi selanjutnya menjadi x
        if ((fa * fx) > 0):
            a = x           # x menjadi batas bawah (a)
            fa = fx         # karena x menjadi a maka f(x) menjadi f(a)
        
        # Apabila f(a).f(x) <= 0, maka x menjadi batas atas di iterasi selanjutnya
        else :
            b = x           # x menjadi batas atas (b)
            fb = fx         # karena x menjadi b maka f(x) menjadi f(b)
    
    # cari akar x yang mana f(x) berpotongan pada sb x di x
    akar = (a + b)/2
    
    # Mengembalikan hasil dalam bentuk sebuah array of string untuk mempermudah pembacaan
    li = ["function f(x) = e^x - x^2 + 3x - 2", f"akar = {akar}", f"iterasi = {iter}"]
    return(li)

# Realisasi (a = -1, b = 0)
lis = biseksi(0, 1)
for x in lis:
    print("==========================================================================================================")
    print(x)