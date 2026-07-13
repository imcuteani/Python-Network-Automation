# A network admin needs to monitor the network devices in real time. Using Python, develop a script periodically 
# pinged each device, checked the response times and logged any anomalies. 
# the script should use ping3 library and csv for logging results. 
# the automated monitoring system should provide timely alerts, allowing the administrator to address issues before they escalated. 


import csv 
import time 

from ping3 import ping, verbose_ping

# 1. simple Ping
delay = ping('google.com')
if delay is not None and delay is not False: 
    print(f"Response time: {delay * 1000:.2f}ms")
else:
    print("Host unreachable") 

#2. Text based standard ping outputs directly over the console 
verbose_ping('google.com')       

# Python library for icmplib (is a fast, pure-python implementation of ICMP). It offers clean object oriented APIS. 

from icmplib import ping 

# returns a host object containing rtt, packets sent/received etc. 

host = ping('8.8.8.8', count=4, interval=1)

print(f"Address: {host.address}")
print(f"Average RTT: {host.avg_rtt}ms")
print(f"packet loss: {host.packet_loss * 100}%")
if host.is_alive:
    print("Host is up")


# using built-in subprocess (no additional installation needed)

# instead of third-party libraries, use the standard subprocess module. 

import platform 
import subprocess 

def quick_ping(host): 
    # determine the current operating system 
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # construct the shell command (to send 1 packet)
    command = ['ping', param, '1', host]

    # Run command and return True if exit code is 0. 

    return subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

# Usage 
is_up = quick_ping('google.com')
print(f"Host status: {'online' if is_up else 'offline'}")

dest_address = "google.com"
file_name    = "trace_output.txt"

# Execute the tracert command 
# using shell=True or parsing a list works, but a list is generally safer
# start the process without waiting for completion
traceresult = subprocess.Popen(
    ['tracert', dest_address],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT, 
    text=True
)

# print the output from the command
# Open file and write line by line
with open(file_name, "w", encoding="utf-8") as file: 
     for line in iter(traceresult.stdout.readline, ''):
      print(line, end='') # print to console
      file.write(line) # save the file

traceresult.stdout.close()