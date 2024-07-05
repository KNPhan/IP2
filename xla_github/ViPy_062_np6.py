import numpy as np

# Initialize the random seed and generate the array
np.random.seed(101)
arr = np.random.randint(1, 4, size=6)

# Create the one-hot encoded array
one_hot = np.zeros((arr.size, arr.max()))

# Assign 1s to the appropriate positions
one_hot[np.arange(arr.size), arr - 1] = 1

# Print the one-hot encoded array
print(one_hot)