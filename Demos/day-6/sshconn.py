import paramiko
import time

# Create SSH client
client = paramiko.SSHClient()

# Set policy to automatically add hosts to known hosts file
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote host
client.connect(
    hostname="192.168.117.128",
    username="anindita",
    password="cisco",
    look_for_keys=False,
    allow_agent=False,
)

# Perform operations on the remote host

# Start an interactive shell
ssh_client = client.invoke_shell()
print("###### Creating loopback interfaces ######")

# ssh_client.send("cisco\n")
ssh_client.send("ifconfig\n")

# Use a for loop and range() to create loopback interfaces
for interface_number in range(0, 1):
    ssh_client.send(f" ip address show 1.1.1.{interface_number}\n")
    

# Wait for the configurations to take effect
time.sleep(1)


# Wait for the output and retrieve it
time.sleep(3)
output = ssh_client.recv(65000)
print(output.decode("ascii"))

# Close the SSH session
ssh_client.close()

# Close the connection
client.close()