import pandas as pd

file = pd.read_csv('kapal_titanic.csv')

cek_umur = file['age']
# print(cek_umur)
# print(type(cek_umur))  # output : <class 'pandas.core.series.Series'>


cek_fare_umur = file[['age', 'fare']]
# print(cek_fare_umur)
# print(type(cek_fare_umur)) # output : <class 'pandas.core.frame.DataFrame'>


# iloc_data = file.iloc[0]
iloc_data = file.iloc[0:11]  # cek index dari 0 sampai 11
iloc_data_akhir = file.iloc[-5:-1] # cek indek dari 5 akhir sampai 1 akhir

iloc_data_index = file.iloc[[0,2,4]] # cek berdasarkan nomor indeks yang diberikan
iloc_data_index_col = file.iloc[[0,2,4],[1,3,6]] # cek berdasarkan nomor indeks dan colom


# print(iloc_data)
# print(iloc_data_akhir)
# print(iloc_data_index)
# print(iloc_data_index_col)


file_baru = pd.read_csv('kapal_titanic.csv', index_col='embarked')
# print(file_baru)

cek_filebaru = file_baru.loc['S']
# print(cek_filebaru)

# cek_filebaru_col = file_baru.loc['S',['age','fare']]
cek_filebaru_col = file_baru.loc[['S','Q'],['age','fare']]

print(cek_filebaru_col)
