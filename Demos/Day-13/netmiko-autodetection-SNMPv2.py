# auto detection with Python SNMP library 

import sys
from getpass import getpass 
from netmiko.snmp_autodetect import SNMPDetect
from netmiko import ConnectHandler

host = "192.168.80.128:5008"
device = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": getpass(),
}

snmp_community = getpass("Enter SNMP community: ")
my_snmp = SNMPDetect(
    host, snmp_version="v2c", community=snmp_community
)

snmp_community = my_snmp.community()
print(snmp_community)

if snmp_community is None:
    sys.exit("SNMP Failed!")

# update the device dictionary with the device_type and connect 

#device["device_type"] = device_type
#with ConnectHandler(**device) as net_connect:
    #print(net_connect.find_prompt())
    net_connect.disconnect()
