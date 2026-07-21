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


# Backup device configuration with Netmiko 

net_connect = ConnectHandler(**cisco_router_telnet)
output = net_connect.send_command('show running-config')
with open('backup_config.txt', 'w') as file: 
    file.write(output)
net_connect.disconnect()    


