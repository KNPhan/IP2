import numpy as np

# Input number n from the keyboard
n = int(input("Enter number n: "))

# Create a numpy array from 0 to n-1
arr = np.arange(n)

# Replace odd values with -1
arr[arr % 2 != 0] = -1

# Print the result
print(arr)
