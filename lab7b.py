#!/usr/bin/env python3
# Author: Melissa Aydin
# Date: 11-11-2026
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py

import numpy as np

# TO DO 1: Copy the code from your lab7a.py file and paste here.
array1 = np.arange(20, 50)
array2 = np.array(list(range(20, 50)))
array3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array4 = np.array([
    [["January", "February"], ["March", "April"], ["May", "June"]],
    [["July", "August"], ["September", "October"], ["November", "December"]]
])

# TO DO 2: Reshape array1 reshapes array2 according to instructions given in readme.md file.
array1 = np.reshape(array1, (5, 6))
array2 = np.reshape(array2, (2, 3, 5))
print("Reshaped array1 (5x6):\n", array1)
print("\nReshaped array2 (2x3x5):\n", array2)

# TO DO 3: Create array5 according to instructions given in readme.md file.
array5 = np.diag([45, 7, 61, 8, 9])
print("\narray5 (5x5 diagonal matrix):\n", array5)

# TO DO 4: Create array6 according to instructions given in readme.md file.
array6 = np.random.randn(7, 7)
print("\narray6 (7x7 normal distribution):\n", array6)
# TO DO 5: Run the script.