#!/usr/bin/env python3
# Author: Melissa Aydin
# Date: 11-11-2026
# Purpose: Create Series.
# Usage: ./lab7e.py

# TO DO 1: Import pandas module.
import pandas as pd

# TO DO 2: Create a series according to instructions given in readme.md file.
grades = pd.Series(
    ["<50", "50-59", "60-69", "70-79", "80-89", "90-100"],
    index=["F", "D", "C", "B", "A", "A+"]
)
print("Grades Series:\n", grades)

# TO DO 3: Perform the operations on this series given in readme.md file.
print("\nValues for indices C and A+:\n", grades[["C", "A+"]])
print("\nValue '60-69' directly:", grades["C"])
print("\nSeries * 2 operation:\n", grades * 2)

# TO DO 4: Run the script.