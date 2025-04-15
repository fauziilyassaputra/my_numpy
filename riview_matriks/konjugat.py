import numpy as np

# membuat matriks kompleks
matriks_kompleks = np.array([[1+2j, 3+4j],
                             [5+6j, 7-8j]])

print("matriks kompleks  :")
print(matriks_kompleks)

# metriks konjugat
matriks_konjugat = matriks_kompleks.conj()
print("matriks konjugat: ")
print(matriks_konjugat)

# matriks transpose konjugat (hermitian):
hermitian_matrix = matriks_kompleks.T.conj()
print("matriks transpose konjugat : ")
print(hermitian_matrix)