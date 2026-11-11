#!/usr/bin/env python3
# Author: Melissa Aydin
# Date: 11-11-2026
# Purpose: Create data frame from CSV file.
# Usage: ./lab7g.py

import pandas as pd
import matplotlib.pyplot as plt

# TO DO 1: create a new data frame from the link of csv file provided in readme.md file.
df = pd.read_csv("imdb_top_250.csv")

# TO DO 2: Perform the operations provided in readme.md file on this data frame.
print("Summary of data:\n", df.describe())
print("\nFirst 10 rows:\n", df.head(10))
print("\nLast 10 rows:\n", df.tail(10))

print("\nEarliest movie year:", df["Year"].min())
print("Latest movie year:", df["Year"].max())

print("\nUnique Genres:\n", df["Genre"].unique())

not_usa_count = (df["Origin"] != "USA").sum()
print("\nMovies not made in USA:", not_usa_count)

top_10 = df.sort_values(by="IMDB rating", ascending=False).head(10)
print("\nTop 10 Highest-Rated Movies:\n", top_10[["Title", "Year", "IMDB rating"]])

def get_decade(year):
    return (year // 10) * 10

df["Decade"] = df["Year"].apply(get_decade)
decade_ratings = df.groupby("Decade")["IMDB rating"].mean()
print("\nMean Rating by Decade:\n", decade_ratings)
print("Best Decade:", decade_ratings.idxmax())

plt.scatter(decade_ratings.index, decade_ratings.values)
plt.title("Mean IMDB Rating by Decade")
plt.xlabel("Decade")
plt.ylabel("Mean Rating")
plt.savefig("lab7g_scatter.png")
plt.show()

# TO DO 3: Run the script.