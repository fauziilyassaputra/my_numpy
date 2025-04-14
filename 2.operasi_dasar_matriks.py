import numpy as np

matriks = np.array([[1,2,3],[4,5,6]])

# Transpose matriks
transpose_matriks = matriks.T
print("transpose matriks : ")
print(transpose_matriks)

# penjumlahan skalar
matriks_plus_scalar = matriks + 10
print("penjumlahan matriks skalar : ")
print(matriks_plus_scalar)

# perkalian elemen matriks
matriks_times_scalar = matriks * 2
print("perkalian matriks skalar : ")
print(matriks_times_scalar)
