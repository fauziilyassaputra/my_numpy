import pandas as pd

file = pd.read_csv('datacsv.csv')

pd.options.display.min_rows = 891
pd.options.display.max_rows = 891

# print(file.info())
# print(file.describe()
print(file.describe(include= "O"))


