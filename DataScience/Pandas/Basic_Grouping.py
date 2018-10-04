"""
Created on Thu Oct  4 10:32:30 2018

@author: benjamin.o.larking
"""
import pandas as pd
import numpy as np

# Where our data is
csv_path="C:\\Users\\benjamin.o.larking\\Documents\\GitHubProjects\\Python\\DataScience\\DataSets\\artwork_data.csv"

csv_df = pd.read_csv(csv_path, index_col = 'id')


######### Find the first aquired art work for each artist ###########
# Create a small copy of the DF
s_df = csv_df.iloc[49990:50019].copy()
grouped = s_df.groupby('artist')
type(grouped)

# After the group by print the name of the grouped object and each row/
for name, group_df in grouped:
    print(name)
    print(group_df)
    break

# Aggregate and find the minimum aquisition year for each artist. 
for name, group_df in grouped:
    min_year = group_df['acquisitionYear'].min()
    print("{} : {}".format(name, min_year))
    
# For each Artist find their first acquisition year
csv_df.groupby('artist')['acquisitionYear'].agg(np.min)
csv_df.groupby('artist')['acquisitionYear'].min()

# Find Titles that appear more than once 
g_titles = csv_df.groupby('title')
title_counts = g_titles.size().sort_values(ascending=False)

condition = lambda x: len(x.index) > 1
dup_titles = g_titles.filter(condition)
dup_titles.sort_values('title', inplace=True)