import numpy as np

# URL of the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Load data using genfromtxt with handling of missing values
data = np.genfromtxt(url, delimiter=',', dtype=float)

# Display the first few rows of the loaded data

arr_without_5th_col = np.delete(data, 4, axis=1)

print(arr_without_5th_col)