import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

# 1. pertukaran baris (baris pertama dan ketiga)
A[[0,2]] = A[[2,0]]
print("pertukaran baris pertama dan ketiga : \n", A)
# 2. perkalian skalar (mengalikan baris kedua dengan 2)
A[1] = A[1] * 2 
print("baris kedua kali 2 : \n", A)
# 3. penjumlahan baris (menambahkan baris pertama ke baris ketiga)
A[2] = A[2] + A[0]
print("baris ketiga ditambah baris pertama: \n", A)

print("matriks setelah operasi elemen adalah :  \n", A)