

from netmiko import ConnectHandler
from datetime import datetime

# define multiple router details with potential authentication errors 

devices = [
    {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": "cisco123",
    },
    {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.138",
    "port": "5009",
    "username": "admin",
    "password": "cisco123",
    },
    {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5002",
    "username": "admin",
    "password": "cisco123",
    }

]

# Get the current timestamp 
time_stamp = datetime.now().strftime("%d-%b-%Y")

# Retrieve the running configurations of each device and save it to a file with a timestamp 

for device in devices:
    net_connect = ConnectHandler(**device)
    print(f"Initiating running config backup for {device['host']}...")
    sh_run = net_connect.send_command('show run', read_timeout=120)

    with open(f"{device['host']}_{time_stamp}.cfg", 'w') as f:
        f.write(sh_run)
        print("Device Backup is saved")
print("Finished Device backup process")        
