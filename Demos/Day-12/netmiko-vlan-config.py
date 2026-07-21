from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
}

net_connect = ConnectHandler(**cisco_router_telnet)
output = net_connect.send_command("show ip interface brief")
print(net_connect.find_prompt())
print(output)

# With NEtmiko VLAN configuration 
# 

net_connect = ConnectHandler(**cisco_router_telnet)
config_commands = [
    'vlan 10',
    'name Automation',
    'exit',
    'vlan 20',
    'name Sales',
    'exit',
] 

output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()