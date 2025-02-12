#   Definisi f(x)
def f(x):
    return(1/(1+x))

#   Metode Simpson 3/8
def simpson_three_eighth(a, b, n):
    h = (b - a) / n
    x = a
    sum = f(a) + f(b)
    for i in range(1, (n-1), 1):
        x = x + h
        if((i % 3) == 0):
            sum += (2 * f(x))
        else:
            sum += (3 * f(x)) 
    return ((3 * h) / 8) * sum

#   Nilai Batas dan Banyak Subinterval
a = 0
b = 1
n = 8

#   Aplikasi
result = simpson_three_eighth(a, b, n)
print(f"Hasil integral dengan metode Simpson 3/8: {result:.5f}")