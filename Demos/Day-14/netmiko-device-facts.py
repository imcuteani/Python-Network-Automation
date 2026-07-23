# collection of device facts - hostname, model, serial and OS/device uptime. 

# once the devices are discovered, it requires to collect comprehensive network documentation, which includes
# hostname, serial number, OS and uptime. 

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

# collection of device internal inventory details 
hostname = net_connect.send_command('show running-config | include hostname', read_timeout=120)
serial = net_connect.send_command('show version | include Serial', read_timeout=120)
uptime = net_connect.send_command('show version | include uptime', read_timeout=120)
os_version = net_connect.send_command('show version | include Cisco IOS', read_timeout=120)

net_connect.disconnect()

# print the device facts 
print(f'HostName: {hostname}')
print(f'Serial: {serial}')
print(f'Uptime: {uptime}')
print(f'OS Version: {os_version}')