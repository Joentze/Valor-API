#import python module
import json
import os 
from API_handler import navigate_to_key

def add_api_to_json(filename, name, body):
    file_data=''
    with open(filename) as file:
        file_data = json.load(file)
        file_data["API"][name] = body        
    with open(filename, 'w') as file:
        json.dump(file_data,file, indent=4)

def remove_data_by_key(filename,key):
    file_data=''
    with open(filename) as file:
        file_data = json.load(file)
        if key in list(file_data['API']):        
            file_data['API'].pop(key)
    with open(filename,'w') as file:
        json.dump(file_data, file, indent=4)

if __name__ == "__main__":
    add_api_to_json('./data/API_collection.json','test',{"data":[1,2,3,4]})
    remove_data_by_key('./data/API_collection.json','test')
