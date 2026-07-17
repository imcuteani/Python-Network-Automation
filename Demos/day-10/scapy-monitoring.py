# Network scanning using Scapy library in Python
#-------------------------------------------------------------------------
# scapy is library supported for python2 and python3. It's used for interacting with the packets on the networks, 
# it has the several functionalities which can easily forge and manipulate the packet. 
# To build a network scanner with Scapy, the Protocol ARP (Address Resolution Protocol) can be used. 
# This can broadcast an exploratory packet across local subnet and maps out every active device's IP address along with its hardware MAC address. 

# About Network Scanning -> Network scanning refers to be scanning of whole network to which we are connected 
# try to find out what are all clients connected to our network. We can identify each and every client using 
# their IP and MAC address. We can also use ARP ping to find out alive systems in the network. 
# To work with Scapy library, it requires special admin priviliges since it uses direct network interface cards (NIC) from the underlying OS. 
# for Linux / MAC, it needs to be executed with admin privilege and for Windows, it needs npacp library as well 

# Steps to create a network scanner 
# 1. Create an ARP packet using ARP() method. 
# 2. Set the network range using variable. 
# 3. Create an Ethernet packet using Ether() method. 
# 4. Set the destination to broadcast using variable hwdst. 
# 5. Combine the ARP request packet and Ethernet frame using "/"
# 6. Send this to your network and capture the response from different devices
# 7. Print the IP and MAC address from the response packets. 

# some important functions for crafting network scanner - 
# 1. ARP(): The function defined in scapy module which allows as to create ARP packets (requests or response). 
# by default, it create the ARP request packet for us. 
import scapy.all as scapy 

# This method provides us the status of the network packet which we have created. It doesn't provide the detailed info about the packet, 
# it just gives the basic indea of what is type of packet
# what is the destination of the packet etc. 
request = scapy.ARP()
print(request.summary())

# 2. show() method -> This method is very similar to summary() method. It gives more detailed information about the packets. 
# the usage of this function is also very much similar to summary() method. 

print(request.show())

# 3. ls() function -> This method is present in scapy class. By using this method, we can see what are the fields 
# that we can set for a specific packet. We can create an ARP packet and with the help pf ls() function, the available 
# fields for this packet. 

print(scapy.ls(scapy.ARP()))

# Python ARP packets implementation 

import scapy.all as scapy 

request = scapy.ARP()

request.pdst = '192.168.31.101/24'
broadcast = scapy.Ether()

# define the broadcast address 
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / request 
clients = scapy.srp(request_broadcast, timeout = 1)[0]
for element in clients: 
    print(element[1].psrc + " " + element[1].hwsrc)
