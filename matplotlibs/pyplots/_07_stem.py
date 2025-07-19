import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = np.random.randint(1, 10, size=10)

plt.stem(x,y, linefmt='--')

plt.xlabel("x")
plt.ylabel("y")
plt.title("stem  plot")
plt.show()
