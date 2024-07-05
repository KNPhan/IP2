import numpy as np
from collections import Counter

# Iris's URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Load data using genfromtxt
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[2], skip_header=True)

# Find the most frequent value and its count
counter = Counter(data)
most_common_value, count = counter.most_common(1)[0]

# Print the result
print(f"{count}, {most_common_value:.2f}")
