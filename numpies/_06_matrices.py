import  numpy as np

data = np.array([[1,2],[3,4], [5,6]])

print(data.min()) # 1
print(data.max()) # 2
print(data.sum()) # 3

data_nonurut = np.array([[1,2],[5,3],[4,6]])
print(data_nonurut)
# output :
# [[1 2]
#  [5 3]
#  [4 6]]
print(data_nonurut.max(axis=0)) # axis 0 = kolom
# output : [5, 6]
print(data_nonurut.max(axis=1)) # axis 1 = baris
# output : [2 5 6]



# Transposing dan reshaping

data_normal = np.array([1,2,3,4,5,6])

data_reshape = data_normal.reshape(2,3)
print(data_reshape)
# output :
# [[1 2 3]
#  [4 5 6]]
data_reshape = data_normal.reshape(3,2)
print(data_reshape)
# output :
# [[1 2]
#  [3 4]
#  [5 6]]


data_transpose = data_normal.reshape(2,3).T
print(data_transpose)
# output :
# [[1 4]
#  [2 5]
#  [3 6]]



