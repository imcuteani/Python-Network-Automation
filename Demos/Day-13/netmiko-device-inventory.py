# Netmiko allows to search for router, switches or firewalls device inventory 

from netmiko import ConnectHandler

import json
import pandas as pd
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from getpass import getpass

# define the device inventory 

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": getpass(),
    
}

try:
 # Use Context manager to auto-class SSH sessions safely
  with ConnectHandler(**cisco_router_telnet) as ssh:
    # Enter enable mode if needed (common in Cisco IOS)
     if cisco_router_telnet["device_type"] == "cisco_ios_telnet":
      ssh.enable()

# fetch the hostname from the prompt automatically 
     host = ssh.find_prompt().rstrip("#>")
# connect to the device      

     net_connect = ConnectHandler(**cisco_router_telnet)
     print(f"Collecting the device hardware data {host}...")
     inventory_output = net_connect.send_command("show inventory", use_textfsm=True, read_timeout=120)
     print(inventory_output)
     version_output = net_connect.send_command("show version", use_textfsm=True, read_timeout=120)
     print(version_output)

# extract the software version from the device inventory list 
     software_version = "Unknown"
     if isinstance(version_output, list) and len(version_output) > 0:
        software_version = version_output[0].get("version", "Unknown")
     else:
        print(f"Could not parse data for {host}..")


except NetmikoTimeoutException:
  print(f"Timeout Error: Unable to reach the device.")

except NetmikoAuthenticationException:
  print(f"Auth Error: Invalid credentials for the device..")

except Exception as e:
  print(f"Unpected error on the device: {e}")  




