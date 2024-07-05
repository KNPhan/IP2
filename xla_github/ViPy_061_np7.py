import numpy as np

# Iris's URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Load data using genfromtxt
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0], skip_header=True)

# Calculate mean, median, and standard deviation
mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data)

# Print the results
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)
