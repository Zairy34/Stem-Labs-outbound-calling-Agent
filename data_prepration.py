# data_preparation.py
import pandas as pd
import json

save_data = r"D:\Artificial-intelligance\Challanges\UI\data\data.json"

def data_creation(path_data):
    df = pd.read_csv(path_data)
    data_dict = df.set_index('ID')['MP3 File Name'].to_dict()
    
    with open(save_data, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)

    print("JSON file has been created and saved")

def getting_values():
    with open(save_data, 'r') as file:
        data = json.load(file)
    
    print("Reading file complete🏃")
    return data  # Return the data

# Only execute this block when running the script directly
if __name__ == "__main__":
    pass
