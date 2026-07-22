# Enablement of Privilege EXEC mode with Netmiko
# Netmiko offers enabling of privilege EXEC mode which grants the elevated privileges, allowing to execute
# wider range of commands. 

from pprint import pprint 
from getpass import getpass

from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": "cisco123",
    "secret" : "cisco"
}

net_connect = ConnectHandler(**cisco_router_telnet)

# invoke the enable() method to elevate privileges
net_connect.enable()
print(net_connect.find_prompt())
output = net_connect.send_command('show run', read_timeout=120)
print(output)
net_connect.disconnect()