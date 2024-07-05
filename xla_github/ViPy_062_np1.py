import numpy as np

# Iris's URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Load data using genfromtxt
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0], skip_header=True)

# Calculate min and max of the column
min_value = np.min(data)
max_value = np.max(data)

# Min-max normalization
normalized_data = (data - min_value) / (max_value - min_value)

# Print the first 5 normalized values as an example
print("First 5 normalized values:")
print(normalized_data[:5])
