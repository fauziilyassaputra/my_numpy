import numpy as np
import matplotlib.pyplot as plt  

# Data acak
x = np.linspace(0,10,100) # 100 nilai x dari 0 hingga 10
y = x**2 #fungsi y = x^2



# menghitung gradient
gradient = np.gradient(y, x)

# plot data dan gradient
plt.scatter(x,y,label="fungsi y = x^2")
plt.plot(x, gradient, label="gradient dy/dx", linestyle='--')
plt.xlabel('x')
plt.ylabel('nilai')
plt.title("Data dan gradientnya")
plt.legend()
plt.grid(True)
plt.show()