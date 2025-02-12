# Fungsi untuk menghitung kesalahan absolut.

# Parameter:
# nilai_eksak (float): Nilai eksak dari pengukuran
# nilai_hampiran (float): Nilai hampiran dari pengukuran

# Return:
# KesalahanRel (float) : Nilai Kesalahan Absolut
def Relatif(NilaiEksak, NilaiHampiran) :
    KesalahanRel = (abs(NilaiEksak - NilaiHampiran) / abs(NilaiEksak)) * 100
    return KesalahanRel
    
# Mendefinisikan nilai eksak dan nilai hampiran
NilaiEksak = 100
NilaiHampiran = 98

# Menghitung kesalahan Relatif
KesalahanRel = Relatif(NilaiEksak, NilaiHampiran)

# Menampilkan hasil
print(f"Kesalahan Relatif: {KesalahanRel} %")