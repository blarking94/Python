"""
Created on Thu Oct  4 10:32:30 2018

@author: benjamin.o.larking
"""
import pandas as pd

# Where our data is
csv_path="C:\\Users\\benjamin.o.larking\\Documents\\GitHubProjects\\Python\\DataScience\\DataSets\\artwork_data.csv"

csv_df = pd.read_csv(csv_path)

# This creates a Series
artists = csv_df['artist']

# This creates a Data Frame 
csv_df[['artist', 'artistId']]

# Find the unique Artists from the Series
pd.unique(artists)
len(pd.unique(artists))

# Returns a boolean Series
s = csv_df['artist'] == 'Bacon, Francis'

# Tells us the count of different values.
s.value_counts()

# Another way of doing this 
artist_counts = csv_df['artist'].value_counts()
artist_counts['Bacon, Francis']

# Row labels are just the position in the index, Column Labels are the position in the column list
# Select by Label - loc - this takes a row indexer and a column indexer
# This returns the artist with index value of 1035
csv_df.loc[1035, 'artist']

# Find all the rows where the artist is Francis Bacon, return all the columns 
csv_df.loc[csv_df['artist'] == 'Bacon, Francis', : ]

# Select by position - iloc - this takes a row indexer and a column indexer
csv_df.iloc[100:300, [0,1,4]]

####### Find the biggest Artwork in the Data Frame ##########

# After being read in the width and height are of type object. They must be converted to numerical values.
pd.to_numeric(csv_df['width']) * pd.to_numeric(csv_df['height'])

# The values however contain null values. Take all the rows for the given column, convert to numericals and ignore null values
df_width = csv_df.loc[:, 'width'] = pd.to_numeric(csv_df['width'], errors='coerce')
df_height = csv_df.loc[:, 'height'] = pd.to_numeric(csv_df['height'], errors='coerce')

area = df_width * df_height

# Add this new Series to the existing Data Frame
csv_df = csv_df.assign(area = area)

csv_df['area'].max()
csv_df['area'].idxmax()
csv_df.loc[csv_df['area'].idxmax(), :]






