import numpy as py
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

# mu=0.0
# sigma=0.1

# s = py.random.normal(mu,sigma,1000)

# plt.hist(s, color="forestgreen")
# plt.xlabel("X")
# plt.ylabel("Frequency")
# plt.title("Randomly sampled Normal distribution ")
# plt.show()

df = pd.read_csv("./data/blood_pressure.csv")
scaling = StandardScaler()
print(scaling.fit_transform(df[['bp_before', 'bp_after']]))