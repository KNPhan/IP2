import numpy as np

# Iris's URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Load data using genfromtxt
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[2], skip_header=True)

# Check the first 4 values of petallength to understand the data
print("First 4 of petallength_col's values:", data[:4])

# Define conditions for categorical conversion
conditions = [
    data < 3,
    (data >= 3) & (data < 5),
    data >= 5
]

# Define corresponding labels
labels = ['small', 'medium', 'large']

# Initialize an empty array for categorical data
categorical_data = np.empty(data.shape, dtype=object)

# Apply conditions to convert to categorical
for i in range(len(conditions)):
    categorical_data[conditions[i]] = labels[i]

# Print the first 4 values of categorical data
print(categorical_data[:4].tolist())


