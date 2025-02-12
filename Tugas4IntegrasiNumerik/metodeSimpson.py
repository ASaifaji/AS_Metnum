#   Definisi f(x)
def f(x):
    return(1/(1+x))

#   Metode Simpson
def simpson_one_third(a, b, n):
    h = (b - a) / n
    x = a
    sum = f(a) + f(b)
    for i in range(1, (n-1), 1):
        x = x + h
        if(i % 2 == 0):
            sum += (2 * f(x))
        else:
            sum += (4 * f(x))
    return ((h / 3) * sum)

#   Nilai Batas dan Banyak Subinterval
a = 0
b = 1
n = 8

#   Aplikasi
result = simpson_one_third(a, b, n)
print(f"Hasil integral dengan metode Simpson 1/3: {result:.5f}")