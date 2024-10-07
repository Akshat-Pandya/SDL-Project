# 2. Reading and Writing Data
# Description: Pandas can read data from various file formats such as CSV, Excel, 
# JSON, and more. Similarly, it can write data back to these formats.
import pandas as pd

# Reading CSV file
df = pd.read_csv('C:/Users/pandy/OneDrive/Desktop/sdl_project/python_SDL_tutorial/pandas/data.csv')
print("type : ",df)

# Writing DataFrame to CSV
df.to_csv('C:/Users/pandy/OneDrive/Desktop/sdl_project/python_SDL_tutorial/pandas/output.csv', index=False)
