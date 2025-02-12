import math

#   Definisi f(x)
def f(x):
    return ((math.sin(x)**2) + math.log(x))

# Metode Trapesium
def trapezium(a, b, n):
    h = (b - a) / n
    sum_ = f(a) + f(b)
    for i in range(1, n):
        sum_ += 2 * f(a + i * h)
    return (h / 2) * sum_

#   Metode Romberg
def romberg_integration(a, b, order):
    
    #   Inisialisasi Matriks
    R = []
    for baris in range(order):
        S = []
        for kolom in range(order):
            S.append(int(0))
        R.append(int(0))
    
    
    for k in range(order):
        n = 2**k
        R[k, 0] = trapezium(a, b, n)
        for j in range(1, k+1):
            R[k, j] = (4**j * R[k, j-1] - R[k-1, j-1]) / (4**j - 1)
    return R[-1, -1]

#   Nilai Batas dan banyak subinterval
a = 1
b = 10
n = 10

order = 4
result = romberg_integration(a, b, order)
print(f"Hasil integral dengan metode Romberg: {result:.5f}")