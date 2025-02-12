import numpy

# Definisi fungsi f(x)
def f(x):
    return (x**2)*numpy.sqrt(x)

# Metode Trapesium
def trapezium(a, b, n):
    h = (b - a) / n
    sum_ = (f(a)/(2*n)) + (f(b)/(2*n))
    for i in range(1, n-1):
        sum_ += (2 * f(a + (i * h))) / (2*n)
    return (b - a) * sum_

# Nilai batas a dan b
a = 1.0
b = 2.8
n = 9

# Hasil perhitungan integral
result = trapezium(a, b, n)
print(f"Hasil integral dengan metode Trapesium: {result:.5f}")
print(10.20934908 - numpy.trapz([1.00,1.58,2.32,3.24,4.35,5.66,7.18,7.38,7.58,7.78],[1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8]))