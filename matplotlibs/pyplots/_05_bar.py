import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])

# tinggi barnya
height = [3,10,15,43,32]

# width: lebar bar
plt.bar(x,height, width=0.8, bottom=2.0, align='center')
plt.title("bar plot")
plt.show()
