import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])
y = np.array([2.0, 2.5, 3.7, 3.2])
y_error = ([0.2, 0.1, 0.3, 0.15])

# xerr, yerr : a float or array-like, fmt: format untuk data point / data lines. ecolor: warna lines errorbar
# capsize: panjang error bar tiap pointnya
plt.errorbar(x, y, yerr=y_error, fmt='o',color='blue', ecolor='red', capsize=5 )

plt.title("Grafik dengan error bar")
plt.xlabel("X")
plt.ylabel("Y & Error")
plt.grid(True)
plt.show()
