import pandas as pd

file = pd.read_csv('datacsv.csv') # total ada 891 data

pd.options.display.min_rows = 891 # agar menghasilkan output seluruhnya tanpa dibatasi
pd.options.display.max_rows = 891

# print(file.info())  # memberikan ringkasan tentang kolom, tipe data , jumlah non-null, dan penggunaan memori
# print(file.describe() # menyediakan statistik deskriptif untuk kolom numerik secara default
print(file.describe(include= "O"))



# reference :
# options = https://pandas.pydata.org/docs/user_guide/options.html

