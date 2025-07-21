import numpy as np

array_examples = np.array([
    [
        [0,1,2,3],
        [4,5,6,7]
    ],
    [
        [0,1,2,3],
        [4,5,6,7]
    ],
    [
        [0,1,2,3],
        [4,5,6,7]
    ]
])


# mengetahui jumlah dimensi pada array
arr_dimension = array_examples.ndim
print(arr_dimension)
# output : 3


# mengetahui angka total pada suatu elemn di dalam array
arr_size = array_examples.size
print(arr_size)
# output : 24


# mengetahui shape pada array
arr_shape = array_examples.shape
print(arr_shape)
# output : (3, 2, 4)


# reshape
a = np.arange(6)
print(a)
# output : [0 1 2 3 4 5]
b = a.reshape(3,2)
print(b)
# output :
# [[0 1]
#  [2 3]
#  [4 5]]

