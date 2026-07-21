from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "localhost",
    "port": "5001",
    "username": "admin",
    "password": "cisco123",
cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5002",
    "username": "admin",
    "password": "cisco123",
}

net_connect = ConnectHandler(**cisco_router_telnet)
output = net_connect.send_command("show ip interface brief")
print(output)
# running multiple commands sequentially 
commands = ['show version', 'show ip route', 'show interfaces']
for command in commands:
    output = net_connect.send_command(command)
    print(output)
net_connect = ConnectHandler(**cisco_router_telnet)
output = net_connect.send_command("show ip interface brief")
print(net_connect.find_prompt())
print(output)


# sending multiple Router config commands 

config_commands = [
    'interface FastEthernet2/0',
    'Description assigned IP to Ethernet',
    'ip address 192.168.2.1 255.255.255.0',
    'no shutdown',
]
output = net_connect.send_config_set(config_commands, read_timeout=120)
print(output)
new_output = net_connect.send_command("show ip interface brief")
print(new_output)
net_connect.disconnect()