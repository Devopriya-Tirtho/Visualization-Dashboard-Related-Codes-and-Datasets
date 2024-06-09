# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:42:22 2024

@author: Hp
"""

import json
import pandas as pd

def create_top_weighted_entries(json_filepath, output_filepath, top_n=10):
    # Load the data
    with open(json_filepath, 'r') as f:
        data = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Group by Source and select the top N weighted entries for each source
    top_entries = df.groupby('Source').apply(lambda x: x.nlargest(top_n, 'Weight')).reset_index(drop=True)

    # Convert back to list of dictionaries
    top_entries_list = top_entries.to_dict(orient='records')

    # Save the new dataset to a JSON file
    with open(output_filepath, 'w') as f:
        json.dump(top_entries_list, f, indent=4)

# Replace 'path_to_your_json_file.json' with the path to your JSON file
# Replace 'output_smaller_json_file.json' with the path where you want the new JSON data to be saved
json_filepath = 'WT_BS_Edge_processed_with_interaction.json'  # Change this to the correct path
output_filepath = 'WT_BS_Edge_processed_with_interaction_Top10.json'  # Change this to the correct path

create_top_weighted_entries(json_filepath, output_filepath)
