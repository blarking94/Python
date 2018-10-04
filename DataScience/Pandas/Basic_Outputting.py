"""
Created on Thu Oct  4 10:32:30 2018

@author: benjamin.o.larking
"""
#Output to Excel, SQL or JSON easily
import pandas as pd
import sqlite3

# Where our data is
csv_path="C:\\Users\\benjamin.o.larking\\Documents\\GitHubProjects\\Python\\DataScience\\DataSets\\artwork_data.csv"

csv_df = pd.read_csv(csv_path, index_col = 'id')

s_df = csv_df.iloc[ 49980:50019, : ].copy()

# Basic Excel
s_df.to_excel('basic.xlsx')
s_df.to_excel('no_index.xlsx', index=False)
s_df.to_excel('columns.xlsx', columns=['artist', 'title', 'year'])


# Multiple Worksheets 
writer = pd.ExcelWriter('multiple_sheets.xlsx', engine='xlsxwriter')
s_df.to_excel(writer, sheet_name='Preview', index=False)
csv_df.to_excel(writer, sheet_name='Complete', index=False)
writer.save()

# Conditional
artist_counts = csv_df['artist'].value_counts()
writer = pd.ExcelWriter('colours.xlsx', engine='xlsxwriter')
artist_counts.to_excel(writer, sheet_name='Artist Counts')
sheet = writer.sheets['Artist Counts']
cells_range = 'B2:B{}'.format(len(artist_counts.index))
sheet.conditional_format(cells_range, {'type': '2_color_scale',
                                       'min_value': '10',
                                       'min_type': 'percentile',
                                       'max_value': '99',
                                       'max_type': 'percentile'
                                       })
writer.save()

# SQL, use sqlalchemy for postgres or mysql
with sqlite3.connect('my_database.db') as conn: 
    s_df.to_sql('Tate', conn)
    
# JSON
s_df.to_json('default.json')
s_df.to_json('table.json', orient='table')