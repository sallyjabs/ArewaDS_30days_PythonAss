# Day 25: 30 days of python programming

# importing the required libraries
import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np

# 1. Read the hacker_news.csv file from data directory

import pandas as pd

df = pd.read_csv('ArewaDS-30days-Of-Python\day_25\hacker_news.csv')
print(df)

# Get the first five rows
first_five_rows = df.head()
print(first_five_rows)

# Get the Last Five Rows
last_five_rows = df.tail()
print(last_five_rows)

# Get the Title Column as Pandas Series
title_series = df['title']
print(title_series)

# Count the Number of Rows and Columns
num_rows, num_columns = df.shape
print(f"Number of rows: {num_rows}") # Number of rows: 20099
print(f"Number of columns: {num_columns}") # Number of columns: 7

# Filter Titles Containing 'Python'
python_titles = df[df['title'].str.contains('Python', case=False)]
print(python_titles) # [160 rows x 7 columns]

# Filter Titles Containing 'JavaScript'
js_titles = df[df['title'].str.contains('JavaScript', case=False)]
print(js_titles) # [170 rows x 7 columns]

# Explore the data and make sense of it
df.info() # i got basic information about the dataframe like rangeIndex, data types, columns
df.describe() # i got descriptive statistics about the dataframe like count, mean, std, min, max