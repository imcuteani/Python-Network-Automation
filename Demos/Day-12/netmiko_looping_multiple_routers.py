from netmiko import ConnectHandler

devices = [
{

    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
},
{
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5006",
    "username": "admin",
    "password": "cisco123",
    }
]

# Looping through multiple routers 

for device in devices: 
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show ip interface brief')
    print(f"Device {device['port']}:\n{output}")
    net_connect.disconnect()
