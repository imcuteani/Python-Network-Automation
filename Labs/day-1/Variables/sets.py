# Sets in Python is a type of data structure which stores the collection of unique items. They're useful for working 
# working with elements like IP addresses, network device ids. 

ip_addr = {"192.168.1.1", "192.168.1.2","10.10.1.1"}
print(type(ip_addr))

# Features of python sets 

# 1. un-ordered collection of elements, cant be accessed by positions. 
# 2. sets are mutable, you can change them after creation. 
# Sets support mathematical functions like union, intersection, difference
# Sets can manage unique items like IP addr, VLAN Ids, network devices etc. 

# adding elements in the set 

addresses = {"192.168.1.1", "192.168.100.1"}
addresses.add("10.34.1.10")
print(addresses)

# update() method which can merge two sets removing the duplicates. 

addresses_1= {"192.168.100.1", "192.168.100.2"}
addresses_2 = {"10.10.2.3", "192.168.1.1", "192.168.10.1"}
addresses_1.update(addresses_2)
print("updated IPs", addresses_1)

addresses_3 = list(addresses_1)
my_address = set(addresses_3)
print("converted updated IPs", my_address)


d1 = {'a1': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d1.update(d2)
print(d1)

# union operator combines all sets and removes the duplicates 

addresses_1= {"192.168.1.1", "192.168.100.1"}
addresses_2 = {"10.10.2.3", "192.168.1.1", "192.168.10.1"}

result = addresses_1 | addresses_2
print(result)

# intersection operator 

# removes the elements which are common in both the sets 

addresses_1= {"192.168.1.1", "192.168.100.1"}
addresses_2 = {"10.10.2.3", "192.168.1.1", "192.168.10.1"} 

intersected_ip = addresses_1 & addresses_2
print(intersected_ip)

# IP address management (IPAM) through python sets 

# Sets can help to manage the IP address pools by finding available IPs in the subnets, overlapping addrress, 
# combining pools. 

ip_pool = {'192.168.1.1', '192.168.1.2', '192.168.1.3'}
assigned_ips = {'192.168.1.2', '192.168.1.4'}

# finding the available IP addresses using the difference operator 

available_ips = ip_pool - assigned_ips
print("Available IPs:", available_ips)

# It will take the available IPs present in the first set and eliminate any duplicates in both first and second set 

# detection of overlapping ip addresses 

overlaps = ip_pool & assigned_ips 
print("overlapping addr", overlaps)

# combining the IP addresses 

print("Combined IPs:", ip_pool | assigned_ips)

# device inventory 

device_inventory_1 = {'Router', 'Firewall', 'Switch', 'Load Balancer'}
device_inventory_2 = {'Firewall', 'Switch', 'Access Point', 'Juniper'}

# finding the common devices using insection operator 

print("Common devices", device_inventory_1 & device_inventory_2)

# finding out the devices which're missing using difference operation 

print("Missing devices", device_inventory_1 - device_inventory_2)