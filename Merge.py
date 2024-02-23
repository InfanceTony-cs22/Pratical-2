import numpy as np

# Create three NumPy arrays of the same shape
array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])

array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])

array3 = np.array([[13, 14, 15],
                   [16, 17, 18]])

# Merge the arrays along a specified axis (axis=0 for vertical, axis=1 for horizontal)
merged_array = np.concatenate((array1, array2, array3), axis=0)

# Display the original arrays and the merged array
print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\nArray 3:")
print(array3)

print("\nMerged Array:")
print(merged_array)
