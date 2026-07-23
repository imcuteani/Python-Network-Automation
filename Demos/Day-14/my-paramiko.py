import paramiko
import time 

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

client.connect(
   
       hostname="192.168.80.128",
       port= "5008",
       username= "admin",
       password= "cisco123",
       look_for_keys=False,
       allow_agent=False,
)

ssh_client = client.invoke_shell()

ssh_client.send("show ip interface brief\n")

time.sleep(3)

output = ssh_client.recv(65000)
print(output.decode("ascii"))

ssh_client.close()

client.close()

