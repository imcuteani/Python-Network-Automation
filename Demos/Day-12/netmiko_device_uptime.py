from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5006",
    "username": "admin",
    "password": "cisco123",
}

# Check device uptime
net_connect = ConnectHandler(**cisco_router_telnet)
output = net_connect.send_command('show version | include uptime')
print(output)
net_connect.disconnect()