# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:36:47 2024

@author: Hp

New Code
"""

import pandas as pd
import json

def scale_value(value, original_min, original_max, new_min, new_max):
    return new_min + (value - original_min) * (new_max - new_min) / (original_max - original_min)

def process_csv_to_json(csv_filepath, output_filepath, chromosome_bins):
    # Load the CSV data
    df = pd.read_csv(csv_filepath)

    # Determine the original range of x and y
    original_x_min = df['X'].min()
    original_x_max = df['X'].max()
    original_y_min = df['Y'].min()
    original_y_max = df['Y'].max()

    # Scale x and y to the range of -200 to 200
    df['X'] = df['X'].apply(scale_value, args=(original_x_min, original_x_max, -200, 200))
    df['Y'] = df['Y'].apply(scale_value, args=(original_y_min, original_y_max, -200, 200))

    # Determine ChID based on the bin ranges
    def determine_chID(node, bins):
        for chID, (start, end) in enumerate(bins, start=1):
            if start <= node <= end:
                return chID
        return None

    df['ChID'] = df['Node'].apply(determine_chID, args=(chromosome_bins,))

    # Create the JSON data
    json_data = []
    for _, row in df.iterrows():
        json_entry = {
            'id': f'Node{int(row["Node"])}',
            'ChID': row['ChID'],
            'x': row['X'],
            'y': row['Y']
        }
        json_data.append(json_entry)

    # Save the JSON data to a file
    with open(output_filepath, 'w') as f:
        json.dump(json_data, f, indent=4)

# Example chromosome bin ranges (these need to be defined as per the specific data)
chromosome_bins = [(1, 404)]  # Adjust this list as needed

# Replace 'path_to_your_csv_file.csv' with the path to your CSV file
# Replace 'output_json_file.json' with the path where you want the JSON data to be saved
csv_filepath = 'WT_BS_Coordinates.csv'  # Change this to the correct path
output_filepath = 'WT_BS_2D.json'  # Change this to the correct path

process_csv_to_json(csv_filepath, output_filepath, chromosome_bins)
