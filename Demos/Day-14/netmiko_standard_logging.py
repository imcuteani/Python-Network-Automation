# Netmiko standard logging 

from netmiko import ConnectHandler

# logging section ### 
import logging

logging.basicConfig(filename="standard.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

## logging section end ##

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": "cisco123",
    "secret" : "cisco",
    
}

net_connect = ConnectHandler(**cisco_router_telnet)
print(net_connect.find_prompt())
net_connect.disconnect()