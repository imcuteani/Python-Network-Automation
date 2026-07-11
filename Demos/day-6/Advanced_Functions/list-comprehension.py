# list comprehension is working with lists with python easier and more efficient. 


# creating a list of MAC addresses 

network_devices = [
    "Router1: AA:BB:CC:DD:EE:FF",
    "Switch1: 11:22:33:44:55:66",
    "Firewall1: 99:88:77:66:55:44",
]

mac_addresses = [device.split(":") [1] for device in network_devices]
print(mac_addresses)