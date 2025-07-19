import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [1,2,3,8,10,12]

# plt.plot(x,y)             # plot x dan y menggunakan default style dan warnanya
# plt.plot(x, y, 'bo')      # plot x dan y dengan tanda lingkaran biru
# plt.plot(y)               # plot y menggunakan x sebagai index array 0..N-1
# plt.plot(y, 'r+')         # menandai menggunakan tanda tambah berwarna merah


# linewidth = ketebalan garis pada plot, markersize = ukuran marker
# plt.plot(x, y, 'go--', linewidth=2, markersize=12)

#  color = mewarnai garis, marker o = titik bulat, style garisnya dashed( putus-putus horizontal )
plt.plot(x, y, color='purple', marker='o', linestyle='dashed', linewidth=2, markersize=12)


plt.show()


# reference :
    # plot = https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
    # Line2D = https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D
