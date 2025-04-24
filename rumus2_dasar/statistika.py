import numpy as np
import matplotlib.pyplot as plt
data = np.array([14,18,24,16,20,22,18])

print(f"mean = {np.mean(data)}")
print(f"median = {np.median(data)}")
print(f"Variance = {np.var(data, ddof=1)}")
print(f"standard deviation = {np.std(data,ddof=1)}")


plt.hist(data, bins=5, edgecolor='black')
plt.title('Histogram Data')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.show()