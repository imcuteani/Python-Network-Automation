# IPv4 network objects are used to inspect and define the IP networks. All of the attributes for address object are also
# valid for network object. 

# network_address -> return the network address 
# broadcast_address -> return the broadcast address for the network 
# netmask -> network mask of the network 
# with_netmask -> return a string containing the mask within the netmask notation
# with_hostmask -> return a string with the mask in host mask notation
# hosts() -> return an itrator over the usable hosts in the network. 
# overlaps -> true if the network is partly or wholelly containing the other networks 
# subnets -> return the subnets which join to make the current network definition dependent on the argument values. 
# supernets-> returns the supernet containing the network definition.

import ipaddress

# initiate the IP4 network 
network = ipaddress.IPv4Network("192.168.1.0/24")

# print the network address of the network
print("Network address of the network: ", network.network_address) 

# print the broadcast address 
print("Broadcast address: ", network.broadcast_address)

# print the network mask 
print("Network mask", network.netmask)

# print with_netmask 
print("with netmask", network.with_netmask)

# print with hostmask
print("with_hostmask", network.with_hostmask)

# print the length of network prefix in bits 
print("length of the network prefix in bits: ", network.prefixlen) 

# print the number of hosts in the network
print("Total number of hosts in the network: ", network.num_addresses)

# print if the network overlaps 192.168.0.0/16
print("If the network is the overlapping: ", network.overlaps(ipaddress.IPv4Network("192.168.0.0/16")))

# print if the network is supernet or subnet of 192.168.0.0/16

print("Supernet: ", network.supernet(prefixlen_diff=1))

# print if the network is subnet of 192.168.0.0/16. 
print("The network is subnet of 192.168.0.0/16", network.subnet_of(ipaddress.IPv4Network("192.168.0.0/16")))

print("The network is supernet of",network.supernet_of(ipaddress.IPv4Network("192.168.0.0/16")))

# comparison the IP network associated with 192.168.0.0/16

print("Compare the network with 192.168.0.0/16:", network.compare_networks(ipaddress.IPv4Network("192.168.0.0/16")))

