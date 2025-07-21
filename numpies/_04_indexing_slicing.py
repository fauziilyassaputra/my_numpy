import numpy as np

data = np.array([1,2,3])

print(data[1]) # 2
print(data[0:2]) # [1, 2]
print(data[1:]) # [2, 3]
print(data[-2:]) # [2, 3]

print("--------------")

a = np.array([[1,2,3,4],[5,6,7,8],[ 9,10,11,12]])
print(a[a < 4])
# output : [1 2 3]

print(a[ a >= 5])
# output : [ 5  6  7  8  9 10 11 12]

print(a[a%2==0])
# output : [ 2  4  6  8 10 12]

print(a[(a > 2) & (a < 11)])
# output : [ 3  4  5  6  7  8  9 10]
