# Netmiko offers a seamless way to enter Global configuration mode of the Cisco routers, where we can 
# make changes to the device settings. 

from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": "cisco123",
    "secret" : "cisco"
}

net_connect = ConnectHandler(**cisco_router_telnet)
net_connect.enable()
net_connect.config_mode()  # Global config mode 

# Create an ACL 'access-list 1 permit any'
net_connect.send_command('access-list 1 permit any', read_timeout=120)

# exit the global configuration mode of the router
net_connect.exit_config_mode()

# fetch the description of device interfaces 
show_output = net_connect.send_command('show interface desc', read_timeout=120)
print(show_output)
net_connect.disconnect() 