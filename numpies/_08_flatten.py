import numpy as np

x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# mengubah menjadi array 1 dimensi (flatten = saat menggunakannya tidak akan mengubah parent arraynya)
print(x.flatten())
# output : [ 1  2  3  4  5  6  7  8  9 10 11 12]


a1 = x.flatten()
a1[0] = 99
print(x) # tidak mengubah x yang mwrupakan parent arraynya

a2 = x.ravel()
a2[0] = 98
print(x) # akan mengubah x yang merupakan parent arraynya
