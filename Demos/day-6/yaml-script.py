# write data to YAML (YET another markup language) script with python 

import yaml 

data = {
    'server': {
        'ip': '192.168.1.1',
        'timeout': 30
    },
    'debug_mode': True
}

# write data structure to output.yaml 
with open("output.yaml", "w") as file: 
    yaml.dump(data, file, default_flow_style=False, sort_keys=False)