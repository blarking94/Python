import pandas as pd 
import numpy as np 


# 3 Rows and 1 Column, this can be turned into a Pandas Series
np_array = np.random.rand(3)

# 3 Rows and 2 Columns, this can be turned into a Pandas DataFrame
np_array_big = np.random.rand(3, 2)

# Create a DataFrame with 3 Rows and 2 Columns
my_first_df = pd.DataFrame(np.random.rand(3,2))

print("\t*** The Random Array ***")
# Print the Frist Element of the Random Array
print(np_array[0])

my_series = pd.Series(np_array)

print("\t*** The Random Array as A Series ***")
# Print the Frist Element of the Series
print(my_series[0])
# Print the whole Series
print(my_series)

# Assign the 3 row series an Index
my_series = pd.Series(np_array, index=["First","Second","Third"])

print("\t*** The Random Array as A Series With Index***")
# Show the New Series, should have an index which is different to 0,1,2
print(my_series)

# We can now refer to the series by index
print(my_series["First"])

# Print all the indexes of the series 
print(my_series.index)

print("\t*** The Random 2 Column Array ***")
# Print the multi dimentional array
print(np_array_big)
# Reference an Object in the multi dimentional array
print(np_array_big[2,1])

print("\t*** Create a Data Frame from the multi dimentional array ***")
# Create a DataFrame from the multi dimentional array
df = pd.DataFrame(np_array_big)

print(df)

# Give column names to the two DataFrame columns
df.columns = ["First", "Second"]

print(df)

# Print a single column, this basically becomes a series
print(df["Second"])