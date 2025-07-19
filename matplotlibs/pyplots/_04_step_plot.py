import numpy as np
import matplotlib.pyplot as plt


x = np.array([1,2,3,4])
y = np.array([6,7,8,9])

# membuat step plot
plt.step(x, y)

plt.title("contoh step")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
