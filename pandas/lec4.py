# What is a Series?
# A Series is a one-dimensional array-like object in Pandas.
# It can hold data of any type (integers, strings, floats, etc.).
# Each value in a Series has a corresponding index.
# It's like a column in a DataFrame but with a single data dimension.

import pandas as pd

# Creating a Series
marks = pd.Series([85, 90, 75, 88], index=['Math', 'English', 'Science', 'History'])

# Accessing data in the Series
print("Marks in English:", marks['English'])

# Performing an operation (e.g., checking which subjects scored more than 80)
high_marks = marks[marks > 80]
print("\nSubjects with marks above 80:")
print(high_marks)

