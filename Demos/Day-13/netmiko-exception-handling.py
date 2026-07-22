# handling exceptions is crucial for network devices, Netmiko provides exception classes to handle common 
# issues such as timeouts and authentication errors. 

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetMikoAuthenticationException

# define multiple router details with potential authentication errors 

devices = [
    {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": "",
    "secret": "abc"
    },
    {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.138",
    "port": "5009",
    "username": "admin",
    "password": "admin",
    },
    {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5002",
    "username": "admin",
    "password": "admin",
    }

]

# Attempt to establish a SSH v2 connection to each device and execute a show command 
for device in devices:
    try: 
         net_connect = ConnectHandler(**device)
         output = net_connect.send_command("show ip int brief", read_timeout=120)
         print(output)
    except NetmikoTimeoutException:
         print(f"Device {device['host']} is not reachable")
    except NetMikoAuthenticationException:
         print(f"Authentication failed for device['username]")          