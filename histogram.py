import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./data/blood_pressure.csv')
# df['sex'].unique()
# df['sex'].value_counts().plot(kind='bar')


plt.hist(df['bp_before'])
plt.show()