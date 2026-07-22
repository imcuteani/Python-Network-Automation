# netmiko allows for applying configuations and saving it to the device level using the save_config method. 

from netmiko import ConnectHandler
from getpass import getpass

device = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": getpass(),
}
commands = ["logging buffered 100000"] 
with ConnectHandler(**device) as net_connect: 
    output = net_connect.send_config_set(commands, read_timeout=240)
    # use the appropriate function for the Netmiko operation
    # commit for Cisco-XR, Juniper-Junos, PA: save config for others 
    output += net_connect.save_config()

# net_connect.disconnect()
print()
print(output)
print()    
