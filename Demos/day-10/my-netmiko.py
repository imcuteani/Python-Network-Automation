from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5000",
    "username": "admin",
    "password": "cisco123",
}

net_connect = ConnectHandler(**cisco_router_telnet)
output = net_connect.send_Command("show ip interface brief")
print(output)
# running multiple commands sequentially 
commands = ['show version', 'show ip route', 'show interfaces']
for command in commands:
    output = net_connect.send_command(command)
    print(output)
net_connect.disconnect()