# RREF

import sympy as sp 

# mendefinisikan matriks menggunakan sympy
A = sp.Matrix([
    [1,3,2],
    [2,6,4],
    [3,9,6]
])

# menghitung RREF
A_rref, pivot_columns = A.rref()

print("Matriks dalam bentuk RREF : ")
sp.pprint(A_rref) #menggunakan pprint agar matriks lebih rapi
print("kolom pivot: ", pivot_columns)
