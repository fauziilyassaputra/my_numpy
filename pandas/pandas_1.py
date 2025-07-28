import pandas as pd
from  sqlalchemy import create_engine

file = pd.read_csv('kapal_titanic.csv')

baca_awal_file = file.head()
# print(baca_awal_file)

baca_akhir_file = file.tail()
# print(baca_akhir_file)

# membuat file csv baru yang berisi data csv lama
file.to_csv("datacsv.csv", index=False) # index false agar index dataframe tidak ikut disimpan di csv
file_baru = pd.read_csv('datacsv.csv')
# print(file_baru)

# mengubah ke excel
file_baru.to_excel('dataexcel.xlsx', index=False, sheet_name='asik')
file_excel = pd.read_excel('dataexcel.xlsx')
# print(file_excel)


# mengubah ke html
file_html = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

type(file_html)
cek_data_html = file_html[0]
# print(cek_data_html)


# mengubah ke data sql
mesin = create_engine('sqlite:///:memory:')
file_baru.to_sql('datasql', con=mesin)
baca_sql = pd.read_sql('datasql', con=mesin)
print(baca_sql)
