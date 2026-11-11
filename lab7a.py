#!/usr/bin/env python3
# Author: Melissa Aydin
# Date: 11-11-2026
# Purpose: Create Arrays.
# Usage: ./lab7a.py

import numpy as np

# TO DO 1: Create array1 and array2 according to instructions given in readme.md file.
array1 = np.arange(20, 50)
array2 = np.array(list(range(20, 50)))
print("array1:\n", array1)
print("\narray2:\n", array2)

# TO DO 2: Create array3 according to instructions given in readme.md file.
array3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\narray3:\n", array3)

# TO DO 3: Create array4 according to instructions given in readme.md file.
array4 = np.array([
    [["January", "February"], ["March", "April"], ["May", "June"]],
    [["July", "August"], ["September", "October"], ["November", "December"]]
])
print("\narray4:\n", array4)