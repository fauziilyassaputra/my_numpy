import numpy as np

#matriks identitas
I = np.eye(3)

# Operasi pertukaran baris pertama dan kedua
E = I.copy()
E[[0,1]] = E[[1,0]]

print("Matriks elementer: \n",I)
print("penukaran baris: \n",E)