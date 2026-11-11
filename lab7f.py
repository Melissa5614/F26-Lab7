#!/usr/bin/env python3
# Author: Melissa Aydin
# Date: 11-11-2026
# Purpose: Create Data Frames.
# Usage: ./lab7f.py

import pandas as pd

# TO DO 1: Create dataframe from provided dictionaries in readme.md file.
dict1 = {"Apple": "Green", "Carrot": "Red", "Radish": "Purple"}
dict2 = {"Okra": "Thin", "Potato": "blob", "Radish": "Round"}
dict3 = {"Apple": 2.1, "Okra": 3.5, "Carrot": 1.3, "Potato": 2.0, "Radish": 3.0}

df1 = pd.DataFrame([dict1, dict2, dict3])
print("DataFrame from dictionaries:\n", df1)

# TO DO 2: create a data frame provided in dataframe.jpg file.
student_data = {
    "student name": ["A", "B", "C", "D"],
    "student marks": [22, 344, 55, 77]
}
df2 = pd.DataFrame(student_data, index=["Maths", "English", "Urdu", "Science"])
print("\nDataFrame from dataframe.jpg:\n", df2)

# TO DO 3: Run the script.