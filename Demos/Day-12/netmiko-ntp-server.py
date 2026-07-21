from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
}

# configure NTP server over the Cisco router 
net_connect = ConnectHandler(**cisco_router_telnet)
config_commands = [
    'ntp server 192.168.2.1',
]

output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()