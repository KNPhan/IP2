import numpy as np

# Iris's URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Load data using genfromtxt
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

# Generate random indices for replacing with np.nan
np.random.seed(42)  # for reproducibility
rows, cols = data.shape
indices = np.random.choice(rows * cols, 10, replace=False)  # Choose 10 random indices
row_indices = indices // cols
col_indices = indices % cols

# Replace selected values with np.nan
data[row_indices, col_indices] = np.nan

# Replace np.nan with 0
data[np.isnan(data)] = 0

# Print the first 5 rows of the modified data as an example
print("Modified data:")
print(data)
