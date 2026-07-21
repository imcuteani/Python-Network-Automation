from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
}

# Setup DHCP Pool configuration
net_connect = ConnectHandler(**cisco_router_telnet)
config_commands = [
    'ip dhcp pool cisco_pool',
    'network 192.168.1.0 255.255.255.0',
    'default-router 192.168.1.1',
    'dns-server 8.8.8.8 8.8.4.4',
]

dhcp_output = net_connect.send_config_set(config_commands)
print(dhcp_output)
net_connect.disconnect()
