# scapy is a powerful python based packet manipulation program and library. It can forge or decode the packets 
# of a wide number of protocols, sending them on the wire, capturing them and can craft custom packets, capturing packets and much more. 

# craft and sending packets 

#from socket import IPPROTO_ICMP

from scapy.all import IP, TCP


# craft an TCP packet on top of IP layer 
packet = IP(dst="8.8.8.8") / TCP(dport=80, flags="S")

# view a detailed layout of the fields
packet.show()

# Sending Packets with Scapy -> Scapy splits sending the packets into basic transmission and transmission receive loops. 

# send() -> send packets at layer 3 IP level without waiting for response. 
# sr1() -> send a layer 3 packet and returns exactly one response. 

from scapy.all import IP, ICMP, sr1

# send a single ICMP ping request and capture the response 

packet = IP(dst="8.8.8.8") / ICMP()

reply = sr1(packet, timeout=2)

if reply: 
    print("Host is online!")
    reply.show() # displays the breakdown of the received packet 
else: 
    print("No response (request timed out)")    