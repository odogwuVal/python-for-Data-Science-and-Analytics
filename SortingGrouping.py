import pandas as pd

data = pd.DataFrame({
    'Name': ['Adaku', 'Alice', 'Mgbeoji', 'Chiamaka', 'Theresa', 'Amaka', 'Adamma', 'Chinelo'],
    'Age': [54, 67, 20, 45, 63, 87, 98, 56],
    'Salary': [20000, 60000, 50000, 100000, 30000, 45000, 670000, 43000],
    'Department': ['Tech', 'Tech', 'Tech', 'Healthcare', 'Operations', 'Operations', 'Tech', 'Tech'],
})

# Ascending order
print(data.sort_values(by='Salary', ascending=True))

# Descending order
print('\n', data.sort_values(by='Salary', ascending=False))

# grouping
print(data.groupby(by='Department')['Salary'].count())
print('average: ', data.groupby(by='Department')['Salary'].mean())
print('minium per department: ', data.groupby(by='Department')['Salary'].min())
print('maximum per department: ', data.groupby(by='Department')['Salary'].max())

# filtering
print(data[data['Salary'] > 50000])
print(data[(data['Salary'] > 50000) & (data['Salary'] < 100000)])
print('\n', data[data['Age'].isin([54,87])])