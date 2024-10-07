# 1. Introduction to Pandas
# Description: Pandas is an open-source Python library used for data manipulation and analysis.
#  It provides data structures like Series and DataFrame that are key for handling 
#  structured data.

import pandas as pd

# Creating a Series
data = pd.Series([1, 2, 3, 4, 5])
print("The value of series : ",data)

# Creating a DataFrame
df = pd.DataFrame(
    {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 35]
    }
)
print("This is a dataframe : ",df)
