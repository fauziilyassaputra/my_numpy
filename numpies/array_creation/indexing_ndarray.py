import numpy as np

# single element indexing

x = np.arange(10)
print(x[2]) # 2
print(x[-2]) # 8



# slicing and striding
# ( start:stop:step )

x = np.array([0,1,2,3,4,5,6,7,8,9])

print(x[1:7:2]) # [1, 3, 5]
# start dari indeks ke-1
# berhenti sebelum indeks ke-7
# ambil setiap 2 elemen


# advance indexing

x = np.arange(10, 1, -1)
print(x) # [10  9  8  7  6  5  4  3  2]
# cek beberapa value x berdasarkan indeks yang dipanggil
print(x[np.array([3,3,1,8])]) # [7 7 9 2]


y = np.arange(35).reshape(5, 7)
print(y)
# output :
# [[ 0  1  2  3  4  5  6]
#  [ 7  8  9 10 11 12 13]
#  [14 15 16 17 18 19 20]
#  [21 22 23 24 25 26 27]
#  [28 29 30 31 32 33 34]]

print(y[np.array([0, 2, 4]), np.array([0, 1, 2]) ]) # [row_indices], [col_indices]
# output : [ 0 15 30]
