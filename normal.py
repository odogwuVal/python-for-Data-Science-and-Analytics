import numpy as py
import matplotlib.pyplot as plt
from scipy.stats import skewnorm
from scipy.stats import expon
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# mu=0.0
# sigma=0.1

# s = py.random.normal(mu,sigma,1000)

# plt.hist(s, color="forestgreen")
# plt.xlabel("X")
# plt.ylabel("Frequency")
# plt.title("Randomly sampled Normal distribution ")
# plt.show()

# df = pd.read_csv("./data/blood_pressure.csv")
# scaling = StandardScaler()
# print(scaling.fit_transform(df[['bp_before', 'bp_after']]))

    # LOG NORMAL DISTRIBUTION
# **********************************
x = skewnorm.rvs(6, size=10000)
# sns.distplot(x)
# plt.show()
# print(x)

data = expon.rvs(scale=1, loc=0, size=1000)
sns.distplot(data, hist=False, kde=False)
plt.show()