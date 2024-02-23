import numpy as np

# Create two NumPy arrays
array1 = np.array(['PHP', 'JS', 'C++'])
array2 = np.array(['Python', 'C#', 'NumPy'])


# Combine the elements using numpy.r_
combined_array = np.r_[array1[:-1],[array1[-1]+array2[0]],array2[1:0]]



# Display the original arrays and the combined array
print("Original arrays:")
print(array1)
print(array2)

print("\nAfter Combining:")
print(combined_array)
