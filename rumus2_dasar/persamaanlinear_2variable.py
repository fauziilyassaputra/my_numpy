import numpy as np
import matplotlib.pyplot as plt 


# matrix koefisien
A = np.array([[2,3],[1,-4]])

#  matrix konstanta
b = np.array([6, -5])

# menyelesaikan sistem persamaan
solution = np.linalg.solve(A,b)

print("solusi: ")
print(f"x = {solution[0]}, y= {solution[1]}")



# fungsi untuk persamaan
x = np.linspace(-5,5,400)
y1 =(6 - 2*x) / 3 #dari persamaan 2x + 3y = 6
y2 = (x + 5) / 4 #dari persamaan x - 4y = -5

# plot kedua garis
plt.plot(x, y1,label="2x+ 3y = 6")
plt.plot(x, y2, label="x - 4y = -5")

# menandai titik sepotong
plt.scatter(3,0, color='red',label="solusi (3,0)")

plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0,  color="black",  linewidth=0.5,linestyle="--")
plt.axvline(0,  color="black",  linewidth=0.5,linestyle="--")
plt.title("visualisasi sistem persamaan")
plt.legend()
plt.grid(True)
plt.show()
