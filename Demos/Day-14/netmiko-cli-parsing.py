# Discovering devices - CDP / LLDP neighbours and subnet scanning. 
# Discovering of network devices is the initial step building a robust network inventory python system. 
# the process involves identifying connected devices like Cisco Discovery Protocol (CDP) and 
# Link Layer Discovery Protocol (LLDP), 
# These protocols are helpful to enable network switches and routers to advertise their identity and capabilities 
# to the neighbours, providing immediate visbility into the network topology. 

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
cdp_output = net_connect.send_command('show cdp neighbors detail')
print(cdp_output)