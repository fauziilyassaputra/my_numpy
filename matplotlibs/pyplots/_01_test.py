import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1) # sintaks = (start, stop, step)
y = np.sin(x) # array y berisi hasil sinus dari tiap nilai x
plt.plot(x, y)
plt.show()
