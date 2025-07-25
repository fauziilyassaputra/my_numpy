import numpy as np
from numpy.random import default_rng

print(np.zeros((2,3)))
# output :
# [[0. 0. 0.]
#  [0. 0. 0.]]

print(np.zeros((2, 3, 2)))
# output :
# [[0. 0.]
#   [0. 0.]
#   [0. 0.]]]


# random method

print(default_rng(42).random((2,3)))
# output :
# [[0.77395605 0.43887844 0.85859792]
#  [0.69736803 0.09417735 0.97562235]]


# indices

print(np.indices((3,3)))
# output :
# [[[0 0 0]
#   [1 1 1]
#   [2 2 2]]
#
#  [[0 1 2]
#   [0 1 2]
#   [0 1 2]]]
