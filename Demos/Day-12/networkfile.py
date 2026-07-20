# python files can be used for loading yaml data through python dictionaries and then exported into to ther formats

import yaml
import json 

# python context manager - "with" keyword helps to manage the resources like files. It helps to let us wotk with it, 
# automatically closes it when we're done, even there's an error. It helps us to perform a graceful shutdown. 
# simplified error handling -> error handling is easier and resource management is enhanced. 
# improved safety ->it reduces the risk of forgetting closing of the file.  
with open('device_vars.yaml', 'r') as yamlfile:
    data = yaml.safe_load(yamlfile)

with open('device_vars.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)   


 # python's json module provides powerful capability for parsing and generating JSON data which's essential for network
 # automation tasks involving REST API, device configuration and data storage. 
 #  read the existing JSON file using python script into a dictionary. 

import json

with open('device_vars.json', 'r') as file:
    devices = json.load(file)

print(data["routers"])
# for loop for retrieve the router device name and IP address 
for device in devices['routers']:
   print(f"Router {device['hostname']}")

output_filename = f"The output file is as router_config.txt"  
with open('output_filename.txt', "w") as outfile:
     simple_device = str(devices)
     outfile.write(simple_device)

print(f"successfully generated staging script for file")     


