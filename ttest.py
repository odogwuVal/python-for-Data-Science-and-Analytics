import numpy as np
from scipy.stats import ttest_1samp

age = [72, 55, 22, 60, 46, 39, 73, 49, 30, 76, 56, 53, 63, 77, 34, 21, 17, 71, 50, 29, 80, 12, 40, 31, 64, 59, 57, 15, 26, 4, 6, 36, 13, 27, 18, 16, 48, 10, 45, 38, 25, 2, 70, 67, 37, 44, 19, 11, 69, 66, 41, 24, 23, 7, 47, 33, 9, 28, 61, 14, 54, 1, 20, 79, 43, 51, 62, 42, 75, 58, 8, 68, 32, 65, 5, 78, 3, 52, 74, 35]
mn = np.mean(age)

sample_age = np.random.choice(age, 10)

tstat,pvalue = ttest_1samp(sample_age, mn)

if pvalue<0.5:
    print("we are rejecting our null hypothesis")
else:
    print("We are accepting our null hypothesis")