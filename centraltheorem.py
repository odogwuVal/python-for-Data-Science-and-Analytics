import numpy as py
import seaborn as sns
import matplotlib.pyplot as plt

sample = py.random.normal(size=1000)

sample_mean = []
for i in range(100):
    s_sample = py.random.choice(sample, size=10, replace=False)
    sample_mean.append(py.mean(s_sample))


sns.distplot(sample_mean)
plt.show()