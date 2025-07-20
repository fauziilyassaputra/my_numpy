import matplotlib.pyplot as plt

# buat figure dengan satu baris dan dua kolom

# matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True,
# width_ratios=None, #height_ratios=None, subplot_kw=None, gridspec_kw=None, **fig_kw)

plt.subplot(1,2,1)
plt.plot([1,2,3],[3,2,1])
plt.title("PLot 1")

plt.subplot(1,2,2)
plt.plot([1,2,3],[1,2,3])
plt.title("plot 2")

plt.tight_layout()
plt.show()
