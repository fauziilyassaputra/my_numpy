import numpy as np

a1 = np.array([
    [1, 1],
    [2, 2]
])

a2 = np.array([
    [3, 3],
    [4, 4]
])

# stack secara vertikal
vertikal = np.vstack((a1, a2))
print(vertikal)
# output :
# [[1 1]
#  [2 2]
#  [3 3]
#  [4 4]]


# stack secara horizontal
horizontal = np.hstack((a1, a2))
print(horizontal)
# output :
# [[1 1 3 3]
#  [2 2 4 4]]
