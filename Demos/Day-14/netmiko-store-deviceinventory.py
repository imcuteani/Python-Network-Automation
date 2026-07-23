# Storing the device inventory data - CSV, Excel, SQLite etc. 

# After collecting detailed device data, storing the device inventory information is crucial for accessibility,
# analysis and integration. 
# various storage options are available from flat files to relational database systems and CMDB. 

# CSV / excel files: These are suitable for small to medium sized inventories and using python's built-in 'csv'
# or 'openpyxl' library. 

# collection of device facts - hostname, model, serial and OS/device uptime. 

# once the devices are discovered, it requires to collect comprehensive network documentation, which includes
# hostname, serial number, OS and uptime. 

from pprint import pprint 
from getpass import getpass
import csv

from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": "cisco123",
    "secret" : "cisco"
}

all_inventory_data = []
net_connect = ConnectHandler(**cisco_router_telnet)

# Loop through devices, execute command and parse with TextFSM and store in CSV file
# collection of device internal inventory details 
for device_info in cisco_router_telnet:
  try:
    with ConnectHandler(**cisco_router_telnet) as net_connect:
      
        hostname = net_connect.send_command('show running-config | include hostname', use_textfsm=True, read_timeout=120)
        model = net_connect.send_command('show version | include Processor board ID', use_textfsm=True, read_timeout=120)
        serial = net_connect.send_command('show version | include Serial', use_textfsm=True, read_timeout=120)
        uptime = net_connect.send_command('show version | include uptime',use_textfsm=True, read_timeout=120)
        os_version = net_connect.send_command('show version | include Cisco IOS',use_textfsm=True, read_timeout=120)

  except Exception as e:
   print(f"Error on {cisco_router_telnet['host']}: {e}")


# print the device facts 
print(f'HostName: {hostname}')
print(f'Model: {model}')
print(f'Serial: {serial}')
print(f'Uptime: {uptime}')
print(f'OS Version: {os_version}')

# write the combined to the output CSV file
if all_inventory_data:
 keys = all_inventory_data[0].keys()
 with open('network_inventory.csv', 'w', newline='', encoding="utf-8") as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames=['Hostname', 'Model', 'Serial', 'Uptime','OS Version'])
    writer.writeheader()
    for device in device_info:
     writer.writerows(device)
    