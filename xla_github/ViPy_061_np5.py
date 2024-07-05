import numpy as np

# Create array arr from 0 to 8 and reshape into a 3x3 matrix
arr = np.arange(9).reshape(3, 3)
print("Original array:")
print(arr)

# Swap columns 0 and 1
arr[:, [0, 1]] = arr[:, [1, 0]]

print("Array after swapping columns 0 and 1:")
print(arr)