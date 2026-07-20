# YAML (Yet another markup language) is a human readbale data serialization standard 
# which is used for configuration files and data exchange. 
# install pyyaml library through Pip using venv

import yaml 

# data to be written in yaml file 

data = {
    'devicename': 'ciscoXE', 
    'deviceos' : 'ios', 
    'ip' : '192.168.224.1', 
    'devicetype' : 'router'
}

# writing to the yaml file 
with open('device.yaml', 'w') as file:
    yaml.dump(data, file)         # Serialize the python dictionary into yaml format 

print("Data has written to the 'device.yaml' file")   

# reading from yaml template 

import yaml 

# reading data from the yaml file 

with open('device.yaml', 'r') as file:
    loaded_data = yaml.safe_load(file)

print("Data read from 'device.yaml':")
print(loaded_data)    