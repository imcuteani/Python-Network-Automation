from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.80.129',
    'port': '5004',
    'username': 'admin',
    'password': 'cisco123',
}

net_connect = ConnectHandler(**cisco_device)
config_commands = [
    'interface GigabitEthernet0/1',
    'description Connected to LAN',
    'ip address 192.168.2.1 255.255.255.0',
    'no shutdown',
]
output = net_connect.send_config_set(config_commands, read_timeout=120)
print(output)
net_connect.disconnect()