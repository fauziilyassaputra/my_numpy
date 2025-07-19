import matplotlib.pyplot as plt

# plt.plot([1,2,3,4],[1,4,9,16], 'bo') # bo = menggunakan titik biru
# plt.axis((0,6,0,20))
# plt.show()

names = ['group_a','group_b','group_c']
values = [1,10,100]

plt.figure(figsize=(9, 3)) # lebar gambar: 9 inch, tinggi gambar: 3 inch
plt.subplot(131) # grid 1 baris x 3 kolom dan subplot pertama
plt.bar(names, values) # menggunakan bar
plt.subplot(132)
plt.scatter(names, values) # menggunakan dot-dot
plt.subplot(133)
plt.plot(names, values) # menggunakan garis
plt.suptitle('Categori Plotting') # judul
plt.show() # tampilkan
