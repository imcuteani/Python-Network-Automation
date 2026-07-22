# with Netmiko, multiple commands can be sent & executed over multiple devices 

from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass('Please enter password for the Router R1!') # prompt for the password securely

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": passwd,   # log in password from getpass
    "secret" : passwd     # enable secret password from getpass  
}

net_connect = ConnectHandler(**cisco_router_telnet)
net_connect.enable() # enable EXEC mode

# execute list of configuration commands which we need to push into the devices 

config_commands = ['interface gi0/0', 'description WAN', 'exit', 'access-list 1 permit any']

# using the send_config_set method, we can send list of commands to the device. The method automatically
# enters Global config mode, executes the commands and exits then the Global config mode. 

net_connect.send_config_set(config_commands, read_timeout=120)

# show commands on the devices 

print(net_connect.send_command('show interface description', read_timeout=120))
print(net_connect.send_command('show access-lists', read_timeout=120))

# finally close the connection
net_connect.disconnect()