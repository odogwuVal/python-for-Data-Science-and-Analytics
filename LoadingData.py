import pandas as pd

csv_data = pd.read_csv('data.csv')
# print(csv_data)
# print(csv_data.head(4))
# print(csv_data.dropna) #drop missing values
# print(csv_data.fillna('NULL')) #fill the missing values with NULL
# print(csv_data.drop_duplicates())
# print(csv_data.info())
print(csv_data.iloc[10]) #access data in specific index

data = pd.DataFrame({'A1': [1, 2, 3],
              'A2': [4, 5, 6],
              'A3': [7, 8, 9]},
              index=['X','Y','Z'])
# print(data)
print(data.loc[:, 'A2'])


# txt_data = pd.read_csv('data.txt', sep=',', header=0)
# print(txt_data)