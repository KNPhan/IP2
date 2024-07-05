import numpy as np

# URL của tập dữ liệu Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Load data using genfromtxt
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 2], skip_header=True)

# Define conditions for filtering
condition_petallength = data[:, 1] > 1.5
condition_sepallength = data[:, 0] < 5.0

# Apply filters to get the final filtered data
filtered_data = data[condition_petallength & condition_sepallength]

# Print the filtered data
print("Filtered data where petallength > 1.5 and sepallength < 5.0:")
print(filtered_data)
