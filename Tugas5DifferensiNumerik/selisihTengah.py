import math

#   f(x)
def f(x):
    return (x**x) + (2*x) + 1

#   f'(x) eksak
def faks(x):
    return math.cos(x)

#   Turunan Selisih Tengah
def selisihTengah(x, h, n):
    if(n == 1):
        return (f(x + h) - f(x + h)) / (2 * h)
    else :
        return (selisihTengah((x + h), h, (n - 1))) - selisihTengah((x - h), h, (n - 1)) / (2 * h)

#   Aplikasi
x = 3       #   Nilai x
h = 2       #   Nilai H
n = 3       #   Tingkat ke-n
print(f"{'{:.10f}'.format(selisihTengah(x, h, n))}")