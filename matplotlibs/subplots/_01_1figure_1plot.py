import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)


fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("simple plot")
plt.show()
