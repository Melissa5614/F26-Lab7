#!/usr/bin/env python3
# Author: Melissa Aydin
# Date: 11-11-2026
# Purpose: Create Histograms.
# Usage: ./lab7h.py

# TO DO 1: Import pandas and matplotlib modules.
import pandas as pd
import matplotlib.pyplot as plt

# TO DO 2: Draw histogram of the data from movies database.
df = pd.read_csv("imdb_top_250.csv")

# TO DO 3: Perform the operations provided in readme.md file on this data.
years = df["Year"].copy()
sorted_years = years.sort_values(ascending=True)
year_counts = sorted_years.value_counts().sort_index()
print("First 10 unique years count:\n", year_counts.head(10))

first_10 = year_counts.head(10)
plt.bar(first_10.index.astype(str), first_10.values, edgecolor="black")
plt.title("Movies Count for First 10 Unique Years")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.savefig("lab7h_histogram.png")
plt.show()

# TO DO 4: Run the script.