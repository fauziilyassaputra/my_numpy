import numpy as np
import matplotlib.pyplot as plt  

# titik titik awal
x1, y1 = 1 , 2
x2, y2 = 4, 6

def garis_lurus(x1,y1,x2,y2):
    # menghitung gradient
    m = (y2 - y1) / (x2 - x1)
    # menghitung titik potong (intersep)
    c = y1 - m * x1
    return m,c

# menghitung gradient dan intercept
m, c = garis_lurus(x1,y1,x2,y2)

# membuat nilai x untuk grafik
x = np.linspace(0,5,100)
y = m * x + c

# plot garis
plt.plot(x,y, label=f"y = {m:.2f}x + {c:.2f}")
plt.scatter([x1,x2],[y1,y2], color="red", label="Titik (x,y)")
plt.xlabel('x')
plt.ylabel('y')
plt.title("grafik garis lurus")
plt.legend()
plt.grid(True)
plt.show()