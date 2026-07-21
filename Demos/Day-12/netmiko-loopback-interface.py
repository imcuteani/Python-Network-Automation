from pprint import pprint 
from getpass import getpass

from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
}

net_connect = ConnectHandler(**cisco_router_telnet)
config_commands = [
    'interface Loopback0',
    'ip address 10.0.0.1 255.255.255.255',
    'no shutdown',
]

output = net_connect.send_config_set(config_commands)
print(output)
cpu_usage = net_connect.send_command('show processes cpu', read_timeout=120, use_textfsm=True)
print()
pprint(cpu_usage)
net_connect.disconnect()