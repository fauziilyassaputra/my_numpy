import numpy as np

# matrix 0 dan 1
print(np.eye(3))
# output :
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


# diagram

print(np.diag([1,2,3]))
# output :
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]
print(np.diag([1,2,3], 1))
# output :
# [[0 1 0 0]
#  [0 0 2 0]
#  [0 0 0 3]
#  [0 0 0 0]]


# general ndarray creation function

print(np.zeros((2,3))) # 2 baris 3 kolom
# output :
# [[0. 0. 0.]
#  [0. 0. 0.]]


print(np.zeros((2, 3, 2)))
# output :
# [[[0. 0.]
#   [0. 0.]
#   [0. 0.]]
#
#  [[0. 0.]
#   [0. 0.]
#   [0. 0.]]]


# np.zeros bisa diganti dengan .ones atau .random

