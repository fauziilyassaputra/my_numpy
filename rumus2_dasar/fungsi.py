import numpy as np;
import matplotlib.pyplot as plt;
# membuat f(x) = x^2 - 4x + 3

# mendefinisikan fungsi secaa numerik
f = lambda x : x**2 - 4*x + 3;

# membuat suatu range nilai x
x = np.linspace(-1,5,200)
y = f(x)

# memplot fungsi
plt.plot(x,y , label='f(x) x^2 - 4x + 3')
plt.xlabel('x');
plt.ylabel('f(x)')
plt.title('plot fungsi')
plt.legend()
plt.grid(True)
plt.show()
