# reads the JSON file with Python 

# json.loads() -> Parses the JSON string into a dictionary 
# json.load() -> reads the JSON file and parses it into a Python dictionary 
# json.dumps() -> converts a python object into a JSON string 
# json.dump() -> Serializes a python object and writes it directly to a JSON file 

import json 

json_string = '{"name": "Cisco", "device": "Router", "ip": "192.168.1.1"}'

data = json.loads(json_string)
print(data["name"])

# open the file and load its contents 
with open('device.json', 'r') as file: 
    data = json.load(file)

# access data like regular dictionary or list 
print(data)    