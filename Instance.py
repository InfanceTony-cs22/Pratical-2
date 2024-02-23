# Importing the NumPy library
import numpy as np

# Creating two NumPy arrays
x = np.array([10, -10, 10, -10, -10, 10])
y = np.array([.85, .45, .9, .8, .12, .6])

# Displaying the original arrays
print("Original arrays:")
print(x)
print(y)

# Counting the number of instances where x equals 10 and y is greater than 0.5
result = np.sum((x == 10) & (y > 0.5))

# Printing the count of instances based on the conditions specified
print("\nNumber of instances of a value occurring in one array on the condition of another array:")
print(result) 
