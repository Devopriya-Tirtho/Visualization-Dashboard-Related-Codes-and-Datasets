# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:27:16 2024

@author: Hp
"""

import json

def minify_json(input_file_path, output_file_path):
    # Read the JSON data from the input file
    with open(input_file_path, 'r') as input_file:
        json_data = json.load(input_file)
    
    # Minify the JSON data by dumping it without indentation
    minified_json_data = json.dumps(json_data, separators=(',', ':'))
    
    # Write the minified JSON data to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(minified_json_data)
    
    print(f"Minified JSON data has been written to {output_file_path}")

# Example usage
input_file_path = 'Brassica_Edge_processed_with_interaction.json'  # Replace with your input file path
output_file_path = 'minified_Brassica_Edge_processed_with_interaction.json'  # Replace with your output file path

minify_json(input_file_path, output_file_path)
