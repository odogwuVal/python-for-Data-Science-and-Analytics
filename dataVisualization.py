import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

x_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_value = [1, 4, 6, 8, 10, 12, 14, 16, 18 ,20]

# plt.plot(x_value, y_value, color='green')
# plt.xlabel(xlabel="X-axis placeholder")
# plt.ylabel(ylabel="Y-axis placeholder")
# plt.title("Title placeholder")
# plt.show()

# plt.scatter(x_value, y_value, color='green')
# plt.xlabel(xlabel="X-axis placeholder")
# plt.ylabel(ylabel="Y-axis placeholder")
# plt.title("Title placeholder")
# plt.show()

# Bar Chart
cat = ["cat", "dog", "horse", "mouse"]
cat_values = [10, 30, 100, 1]

# plt.bar(cat, cat_values, color="green")
# plt.xlabel(xlabel="Animals")
# plt.ylabel(ylabel="Weight")
# plt.title("Weight per animal")
# plt.show()

# Histogram
x_normal = np.random.normal(0, 1, 10000)
plt.hist(x_normal, color="forestgreen")
plt.xlabel("X")
plt.ylabel("Frequency")
plt.title("Randomly sampled Normal distribution ")
plt.show()

# Population distribution
x_value = np.arange(-5, 5, 0.01)
y_value = norm.pdf(x_value)

counts, bin, ignored = plt.hist(x_normal, 30, density=True, color="purple", label="Sampling Distribution")
plt.plot(x_value, y_value, color="y", linewidth=2.5, label="Population Distribution")
plt.ylabel("Probability")
plt.legend()
plt.show()