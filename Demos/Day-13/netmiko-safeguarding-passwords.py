# Safeguarding passwords in Network Automation with Python's getpass

# storing passwords or secrets as plain text is a big security risk. Python provides the getpass library. 
# The getpass library allows to prompt the user for sensitive information such as passwords without 
# echoing their input to the terminal. 
# the password remains hidden from the view enhancing the security. 

from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass('Please enter password for the Router R1') # prompt for the password securely

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": passwd,   # log in password from getpass
    "secret" : passwd     # enable secret password from getpass  
}

net_connect = ConnectHandler(**cisco_router_telnet)
net_connect.enable()  # Enter Privilege EXEC mode

output = net_connect.send_command('show interface desc', read_timeout=120)
print(output)

net_connect.disconnect()