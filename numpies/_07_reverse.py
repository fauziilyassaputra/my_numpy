import numpy as np

# reversing 1D array
arr = np.array([1,2,3,4,5,6,7,8])
reversed_arr = np.flip(arr)
print(reversed_arr)
# output : [8 7 6 5 4 3 2 1]

# reversing 2D array
arr_2d = np.array([[1,2,3,4],[5,6,7,8], [9,10,11,12]])
reversed_arr = np.flip(arr_2d)
print(reversed_arr)
# output :
# [[12 11 10  9]
#  [ 8  7  6  5]
#  [ 4  3  2  1]]
