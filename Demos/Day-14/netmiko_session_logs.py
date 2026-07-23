# session logs with Netmiko for Cisco IOS device 
# To create a session log file with Netmiko, you can pass the session_log argument into the ConnectHandler dictionary to
# capture all underlying SSH/Telnet read and write operations. 

# this script establishes a connection to a Cisco IOS device and logs the raw interaction directly to a local file named 'session.log'
# 
#  

from netmiko import ConnectHandler

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": "cisco123",
    "secret" : "cisco",
    "session_log": "session.log",   # path to the output log file 
}

# establish the router device connection and send a command 

with ConnectHandler(**cisco_router_telnet) as net_connect: 
    net_connect.enable()
    output = net_connect.send_command("show ip interface brief", read_timeout=120)
    print("Command executed successfully")