"""
Created on Thu Oct  4

@author: benjamin.o.larking

"""
from numpy import np
from pandas import pd
import matplotlab as plt
import os

csv_path = os.path.join("..", "DataSets", "weather.csv")

# A small data frame for our demo
df = pd.read_csv(csv_path).head()

#########################################################################
############################ Selecting ##################################
#########################################################################

# Convert to a temperature series and get element in position 1
df['TEMP'][1]

# .T means to Transpose the Data Frame. Put the columns as indexs and rows as columns 
dft = df.T
dft[2]
# This is a range of numbers 1 - 5
dft.columns
# get the time for the second column. What was originally row 2
# The key point here is that earlier we had to use the column name to reference the column. Now we can reference it with a number
dft[2]['TIME']
dft[2][2]

# The double brackets tell us that we're indexing into the Data Frame and then passing a python list to get the list of columns we want
df[['PRESSURE', 'TIME', 'TEMP']]
# Select the Time Series then query the series again with a python list to find index's 3,1,4
df['TIME'][[3,1,4]]

# Selecting slices, select row 2 to 4
df[2:4][['TEMP', 'PRESSURE']]
dft[3:][[2,3]]
dft['TEMP' : 'PRESSURE'][[2,3]]

df['PRESSURE'][:4]
dft[:2]
dft['TEMP' : 'PRESSURE']

#########################################################################
############################ Using Loc and ILoc #########################
#########################################################################

capitals = pd.DataFrame(
        [
                ["Ngerulmud", 391,1.87],
                ["Vatican City", 826,100],
                ["Yaren", 1100,10.91],
                ["Funafuti", 4492,45.48],
                ["City od San Marino", 4493],
        ],
                index = ["Palau", "Vatican City", "Nauru", "Tuvalu", "San Marino"],
                columns = ["Capital", "Population", "Percentage"]
        )