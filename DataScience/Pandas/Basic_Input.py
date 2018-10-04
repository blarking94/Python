"""
Created on Thu Oct  4 10:32:30 2018

@author: benjamin.o.larking
"""
import pandas as pd
import json
import os

############################################################################################
######################### Read CSV #########################################################
############################################################################################

# Where our data is
csv_path="C:\\Users\\benjamin.o.larking\\Documents\\GitHubProjects\\Python\\DataScience\\DataSets\\artwork_data.csv"

# Read just 5 first rows of the CSV, use ID as the index
csv_df = pd.read_csv(csv_path, nrows = 5, index_col = 'id')

# Read just 5 first rows of the CSV, select only ID and Artist, use the ID as the index
csv_df = pd.read_csv(csv_path, nrows = 5, index_col = 'id', usecols = ['id', 'artist'])

# Use an array to state which columns we want to read
COLS_TO_USE = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

csv_df = pd.read_csv(csv_path, nrows = 5, index_col = 'id', usecols = COLS_TO_USE)


############################################################################################
######################### Read JSON ########################################################
############################################################################################

# Simple JSON data
records = [("Espresso", "$5"),("Flat White", "$10")]

json_df = pd.DataFrame.from_records(records)

json_df = pd.DataFrame.from_records(records, columns = ["Coffee", "Price"])

KEYS_TO_USE = ['id', 'all_artists', 'title', 'medium', 'acquisitionYear', 'height', 'width', 'units']

def get_records_from_file(file_path, keys_to_use):
    # Process a single file
    with open(file_path) as artwork_file:
        content = json.load(artwork_file)
        
    record = []
    for field in keys_to_use:
        record.append(content[field])
        
    return tuple(record)

# First JSON
SAMPLE_JSON_PATH = "C:\\Users\\benjamin.o.larking\\Documents\\GitHubProjects\\Python\\DataScience\\DataSets\\artwork_data_json\\a\\000\\a00001-1035.json"

sample_record = get_records_from_file(SAMPLE_JSON_PATH, KEYS_TO_USE)

# Read All JSON Files
def read_artworks_from_json(keys_to_use):
    # Define the root directory and find all the json files in this directory
    JSON_ROOT = "C:\\Users\\benjamin.o.larking\\Documents\\GitHubProjects\\Python\\DataScience\\DataSets\\artwork_data_json"
    artworks = []
    for root, _, files in os.walk(JSON_ROOT):
        for f in files:
            if f.endswith('json'):
                record = get_records_from_file(os.path.join(root, f), keys_to_use)
                artworks.append(record)
            # We put a break here to just read the first file in each directory - otherwise read would take ages on a local machine. 
            break
        
    json_df = pd.DataFrame.from_records(artworks, columns = keys_to_use, index = 'id')
    
    return json_df

json_df = read_artworks_from_json(KEYS_TO_USE)






