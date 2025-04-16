import numpy as np
import sympy as sp

A = np.array([[2,4,-2,2],
              [4,9,-3,8],
              [-2,-3,7,10]], dtype=float)

#konversi ke matriks sympy agar bisa menggunakan fungsi rref()
A_sym = sp.Matrix(A)

# dapatkan eselon  baris tereduksi
rref_matrix, pivot_columns = A_sym.rref()

# cetak hasilnya
print("Matriks dalam bentuk eselon baris tereduksi :")
print(rref_matrix)

