#  Netmiko & Paramiko difference in real time use cases 

# 1. Abstraction level -> Netmiko is high level wrapper and Paramiko is low level toolkit. 
# 2. Multivendor hardware -> Netmiko supports multi-vendor hardwares but Paramiko is linux and unix servers. 
# 3. Protocols -> Netmiko supports SSHv2, Telnet and Serial ports. Paramiko supports only SSHv2. 
# 4. CLI prompts -> Netmiko automatic (waits for terminal prompts), Paramiko os manual (requires time delays)
# 5. Priviledges -> Built-in .enable() and config modes, but Paramiko is for manual command entry. 