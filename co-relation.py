import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./data/Iris.csv')
print(df.corr(numeric_only=True))
sns.pairplot(df)
plt.show()