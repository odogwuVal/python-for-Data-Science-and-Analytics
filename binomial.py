from scipy.stats import binom

sum=0
for i in range(3,6):
    s = binom.pmf(k=i, n=5, p=0.75)
    sum += s

print(sum)