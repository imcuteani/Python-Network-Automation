# Using Netmiko, collecting device facts with TTP 

from netmiko import ConnectHandler 
from getpass import getpass
from pprint import pprint

cisco1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": getpass(),
    
}

# write the device facts collection to a file 
ttp_raw_template = """
 interface {{ interface }}
  description {{ description }}
"""



# apply device command with TTP CLI output parsing 
command = "show run | s interfaces"
with ConnectHandler(**cisco1) as net_connect: 
    # use TTP to retrieve the structured device data 
     output = net_connect.send_command(command, use_ttp=True, ttp_template="show_run_interfaces.ttp", read_timeout=120)
     #genie_output = net_connect.send_command(command, use_genie=True, read_timeout=240)
# write the device inventory output 
with open ("show_run_interfaces.ttp", "w") as writer: 
    writer.write(ttp_raw_template)   

print()
pprint(output)
#pprint(genie_output)
print()
net_connect.disconnect()