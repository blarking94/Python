"""
Created on Thu Oct  4

@author: benjamin.o.larking

When we're first loading in a new Series or DataFrame we should take some steps to understand the data better. 

These first steps might include calling the shape, info, head or tail and describe functions to get a better understanding
of how many rows and columns there are, the data types for each column and even what some of the data actually looks like.
"""

import numpy as np
import pandas as pd
import matplotlib as plt
import os

csv_path = os.path.join('..', 'DataSets', 'weather.csv')

df = pd.read_csv(csv_path)

# Tell us the size of the Data Frame and a little more!
df.shape
df.info()

# Look at the Head and Tail of the Data Frame 
df.head(10)
df.tail(10)

# Basic Statistical Data 
df.describe(include='all')
df.mean()
df.max()
df['PRESSURE'].min()
df['TEMP'].mode()
df['TEMP'].plot()
# check out the histogram 
df['TEMP'].plot.hist()
# use the bins variable to make it more fine grained  
df['TEMP'].plot.hist(bins=100)




