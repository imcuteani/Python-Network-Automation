from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
}
# Apply ACL configuration
net_connect = ConnectHandler(**cisco_router_telnet)
config_commands = [
    'access-list 100 permit ip any any',
    'access-list 101 deny ip 192.168.1.0 0.0.0.255 any',
]
output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()

# BGP Configuration 

net_connect = ConnectHandler(**cisco_router_telnet)
config_commands = [
    'router bgp 65000',
    'neighbor 192.168.2.1 remote-as 65001',
    'network 192.168.1.0 mask 255.255.255.0'
]

output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()