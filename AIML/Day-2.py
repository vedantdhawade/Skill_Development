# Create a 1D array with numbers from 10 to 20.
import numpy as np # type: ignore
arr = np.arange(10,21)
print(arr)

# Create a 3x3 matrix of zeros.
arr1 = np.zeros((3,3))
print(arr1)

# Add two 2D arrays of size 2x2.
arr1 = np.array([[1,2,3],[1,3,4]])
arr2 = np.array([[1,2,3],[1,3,4]])
print(arr1 + arr2 )

# Multiply a 1D array by a scalar (e.g., multiply [1, 2, 3] by 5).

arr3 = arr1 * 3
print(arr3)

# Create a 3x3 array and print the second row.

arr4 = np.array([[1,2,3],[4,6,8],[2,6,8]])
print(arr4[1])

# Print the last column of the array.

print(arr4[:,1])

# Compute the mean and standard deviation of a 1D array.

print(np.mean(arr4))
print(np.std(arr4))

# Apply the exponential function to an array of numbers.

print(np.exp(arr4))

# Create a 4x4 matrix and compute its transpose.

print(arr4.T)

# Normalize a 1D array (subtract the mean and divide by the standard deviation).

print((arr4 - np.mean(arr4))/np.std(arr4))