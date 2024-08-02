import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_data = pd.read_csv('data.csv')
# print(csv_data)
# print(csv_data.head(4))
# print(csv_data.dropna) #drop missing values
# print(csv_data.fillna('NULL')) #fill the missing values with NULL
# print(csv_data.drop_duplicates())
# print(csv_data.info())
# print(csv_data.iloc[10]) #access data in specific index

# data = pd.DataFrame({'A1': [1, 2, 3],
#               'A2': [4, 5, 6],
#               'A3': [7, 8, 9]},
#               index=['X','Y','Z'])
# # print(data)
# print(data.loc[:, 'A2'])


# txt_data = pd.read_csv('data.txt', sep=',', header=0)
# print(txt_data)

# plt.boxplot(data=csv_data, x=csv_data['StudentID'])
# print(csv_data['StudentID'].describe())
# q1 = csv_data['StudentID'].quantile(0.25)
# q3 = csv_data['StudentID'].quantile(0.75)
# iqr = q3-q1

# upper_bound = q3 + 1.5*iqr #data above this is the upper outlier
# lower_bound = q1 - 1.5*iqr #data below this is the low outlier

# print("upper bound: ", upper_bound)
# print("25% quantile is: ", q1)
# print("\n", "75% quantile is: ", q3)
# print("\n", "IQR is: ", iqr)
# print("lower bound: ", lower_bound)

# filter = csv_data["StudentID"] < upper_bound
# print(csv_data[filter])

# plt.show()

# skewness
dict={'Name':['Tom','Tom','Ricky','Vin','Steve','Smith','Jack','Lee','Chanchal','Gasper','Naviya','Andres'],
   'Age':[25,26,25,23,30,29,23,34,40,30,51,46],
   'Rating':[4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65]}

df = pd.DataFrame(dict)
print(df.skew(numeric_only=True))


#0- => no skewness
#+- => right handside tail
#- => left handside tail