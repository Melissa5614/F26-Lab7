#!/usr/bin/env python3
# Author: Melissa Aydin
# Date: 11-11-2026
# Purpose: Slicing 2D NumPy Arrays.
# Usage: ./lab7d.py

import numpy as np

# Creating a 2D NumPy array
arr_2d = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])
print("Original 2D Array:\n", arr_2d)

# Slice the first two rows and the last three columns of arr_2d
slice_1 = arr_2d[:2, -3:]
print("\nslice_1:\n", slice_1)

# Extract the middle 2x2 subarray (elements 70, 80, 120, 130)
slice_2 = arr_2d[1:3, 1:3]
print("\nslice_2:\n", slice_2)

# Slice every other row and every other column from arr_2d
slice_3 = arr_2d[::2, ::2]
print("\nslice_3:\n", slice_3)