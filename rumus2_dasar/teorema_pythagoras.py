import math
import matplotlib.pyplot as plt  

# panjang sisi sisi segitiga siku siku
a = 3 # sisi horizontal
b = 4 # sisi vertikal

# menghitung sisimiring menggunakan math
c = math.sqrt(a**2 + b**2)

# menampilkan hasil perhitungan
print(f"Sisi a: {a}")
print(f"sisi b: {b}")
print(f"sisi miring (c) : {c:2f}")

# membuat koordinat segitiga
x_coords = [0,a,0,0]
y_coords = [0,0,b,0]

# membuat plot segitiga
plt.figure(figsize=(6,6))
plt.plot(x_coords,y_coords,marker='o',label="segitiga siku-siku")

# menambahkan label sisi pada grafik
plt.text(a / 2, -0.5, f"a = {a}", ha="center", fontsize=10, color='blue')
plt.text(-0.5,  b / 2, f"b = {b}", va="center", fontsize=10, color='blue')
plt.text(a / 2, b/ 2, f"c= {c:.2f}", fontsize=10, color='red')

# mengatur tampilan grafik
plt.title("visualisasi teorema pythagoras")
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0,color='black', linewidth=0.5,linestyle="--")
plt.axvline(0,color='black', linewidth=0.5,linestyle="--")
plt.grid(True)
plt.axis('equal')
plt.legend(["sisi segitiga"])
plt.show()
