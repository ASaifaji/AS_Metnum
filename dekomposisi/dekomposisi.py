# Kamus
A = [[1,2,3],[4,6,9],[3,7,1]]  # Bakal matriks A
b = [19, 60, 46]
L = [[1,0,0],[0,1,0],[0,0,1]] # Matriks Identitas

# Prosedur Mengubah matriks A menjadi I.A -> L.U
# Menghasilkan nilai L dan U
# A terdefinisi
def ubah(A,L):
  for i in range(2):
    for j in range(1,3):
      if(i == 1 and j == 1):
        continue
      temp = A[j][i] / A[i][i]
      L[j][i] = temp
      for x in range(3):
        A[j][x] = A[j][x] - (temp*(A[i][x]))


# Fungsi mengembalikan nilai y
def findy(L,b):
  y = []
  y.append(b[0])
  y.append(b[1] - (L[1][0]*y[0]))
  y.append(b[2] - (L[2][0]*y[0]) - (L[2][1]*y[1]))
  return y

# Fungsi Mengembalikan nilai x
def findx(U,y):
  x = [0,0,0]
  x[2] = (y[2]/U[2][2])
  x[1] = ((y[1] - (U[1][2]*x[2]))/U[1][1])
  x[0] = ((y[0] - (U[0][2]*x[2]) - (U[0][1]*x[1]))/U[0][0])
  return x

# Prosedur input persamaan linear
# Masukkan koefisien variabel x ke A
# Masukkan konstanta ke b
# def input(A,b):
#   for row in range(3):
#     print(f"\nPersamaan linear ke-{row + 1}")
#     a = []
#     for column in range(3):
#       a.append(int(input(f"Masukkan koefisien x{column + 1} dari persamaan ke-{row + 1}:")))
#     A.append(a)
#     b.append(int(input(f"Masukkan konstanta dari persamaan ke-{row}:")))

# def reset(A,b):
#   A = []
#   b = []

# Fungsi main dekomposisi LU
def main(A,b,L):
  ubah(A,L)
  y = findy(L,b)
  x = findx(A,y)
  for i in range(3):
    print(f"Y{i + 1} = {y[i]}")
  for i in range(3):
    print(f"X{i + 1} = {x[i]}")

# Aplikasi
main(A,b,L)