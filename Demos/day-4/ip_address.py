# in computer networking, it's a way to identify numbers related to selected computer or network. IP address is helpful to allow
# IPv4 and IPv6 modules to create, manipulate and operate the addresses. 
# 

import ipaddress

# Creating an object of IPv4Address class and initialize it with an IPv4 address. 

ip = ipaddress.IPv4Address('100.1.1.1')

# print total number of bits in the IP
print("Total number of bits in the ip: ", ip.max_prefixlen)

# Print true if the IP address is reserved for multicast use. 
print("Is multicast", ip.is_multicast)

# print True if the IP address can be allocated for private networks 
print("Is private IP: ", ip.is_private)

# Print True if the IP address is global 
print("Is global: ", ip.is_global)

# Print True if the IP address is unspecified 
print("Is unspecified: ", ip.is_unspecified)

# print True if the IP address is IETF reserved 
print("Is reserved: ", ip.is_reserved)

# print True if the address is loopback address
print("Is loopback: ", ip.is_loopback)

# print True if the IP address is link-local
print("Is link local:", ip.is_link_local)

# next IP address 
ip1 = ip + 1 
print("next ip", ip1)

# previous IP address 
ip2 = ip - 1 
print("Previous IP: ", ip2)

# print True if IP1 is greater than IP2 
print("Is IP1 greater than IP2:", ip1 > ip2)

