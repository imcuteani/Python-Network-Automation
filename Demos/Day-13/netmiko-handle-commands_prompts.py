from netmiko import ConnectHandler
from getpass import getpass

cisco_router_telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.128",
    "port": "5008",
    "username": "admin",
    "password": getpass(),
}

command = "del flash:/test4.txt"
net_connect = ConnectHandler(**cisco_router_telnet)

# CLI interaction is as follows 
# cisco_router_telnet#delete flash:/testb.txt
# delete filename [testb.txt]?
# delete flush:/testb.txt? [confirm]y
# 
# use send_command and the expect_string argument 
# expect_string uses Regex patterns. Netmiko will move on the next command when the 
# expect_string is detected. 
# 
# strip_prompts=False and strip_command=False make the output easier to read in this context. 
# 
output = net_connect.send_command(
    command_string=command,
    expect_string=r"Delete filename",
    strip_prompt=False,
    strip_command=False,
    read_timeout=120
)  

output += net_connect.send_command(
    command_string="\n",
    expect_string=r"confirm",
    strip_prompt=False,
    strip_command=False,
    read_timeout=120
)

output += net_connect.send_command(
    command_string="y",
    expect_string=r"#",
    strip_prompt=False,
    strip_command=False,
    read_timeout=120
)

# disconnect the device 
net_connect.disconnect()

print()
print(output)
print()