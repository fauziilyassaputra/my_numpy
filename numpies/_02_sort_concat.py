import numpy as np


# sorting
arr = np.array([4,3,2,7,8,6,8,1,9])
arr_sort = np.sort(arr)
print(arr_sort)
# output : [1 2 3 4 6 7 8 8 9]


#concatenate (menggabungkan)
a = np.array([10,20,30,40])
b = np.array([50,60,70,80])

arr_concat = np.concatenate((a,b))
print(arr_concat)
# output : [10 20 30 40 50 60 70 80]

c = np.array([[1,2], [3,4]])
d = np.array([[5,6]])
arr_concat2 = np.concatenate((c,d), axis=0)
print(arr_concat2)
# [
# [1 2]
# [3 4]
# [5 6]
# ]
