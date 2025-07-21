import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# dengan subplot_kw, semua subplot otomatis dalam koordinat polar, tidak perlu membuat satu-persatu
fig, axs = plt.subplots(2,2 , subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

# [0,1] dan [1,0] tetap dibuat namun kosong

plt.show()
