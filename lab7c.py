#!/usr/bin/env python3
# Author: Melissa Aydin
# Date: 11-11-2026
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

import numpy as np

# TO DO 1: Create numArray according to instructions given in readme.md file.
numArray = np.random.randint(1, 100, 100)
print("Original numArray:\n", numArray)

# TO DO 2: Perform the operations on numArray given in readme.md file.
print("\nFirst 10 values:\n", numArray[:10])
print("\nLast 10 values:\n", numArray[-10:])
print("\n30 values starting from index 21:\n", numArray[21:51])

numArray[50:66] = 101
print("\nnumArray after changing indices 50 to 65 to 101:\n", numArray)

# TO DO 3: Run the script.