import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./data/Iris.csv')
# df['Species'].value_counts().plot(kind='bar')
# plt.show()
# plt.hist(df['SepalLengthCm'], density=False)
# plt.show()

# plt.scatter(df['SepalLengthCm'],df['SepalWidthCm'])
# plt.show()

sns.pairplot(df)
plt.show()