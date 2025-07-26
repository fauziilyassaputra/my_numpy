import numpy as np




a = np.array([1.0, 2.0, 3.0])
# b = np.array([2.0, 2.0, 2.0])
b = 2.0
# meskipun berbeda dimensi tetap bisa dikalikan

result = a * b
print(result)



a = np.array([[ 0.0,  0.0,  0.0],

              [10.0, 10.0, 10.0],

              [20.0, 20.0, 20.0],

              [30.0, 30.0, 30.0]])

b = np.array([1.0 , 2.0, 3.0])
# b = np.array([1.0 , 2.0, 3.0, 4.0]) # Error

print(a + b)
