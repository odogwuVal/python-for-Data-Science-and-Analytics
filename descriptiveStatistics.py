import numpy as np
from scipy import stats
import pandas as pd

data = [20, 5, 100, 30, -50, 20, 62]
mean_ = np.mean(data)
print("Mean of the array is: ", mean_)

median_ = np.median(data)
print("Median of the array is: ", median_)

mode_ = stats.mode(data)
print("Mode of the array is: ", mode_)

variance_ = np.var(data)
print("variance of the array is: ", variance_)

std_ = np.std(data)
print("standard deviation of the array is: ", std_)

# Loading CSV files with data
csv_data = pd.read_csv("data.csv")
print(csv_data.describe())