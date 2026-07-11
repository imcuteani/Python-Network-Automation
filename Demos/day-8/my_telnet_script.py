import getpass
import telnetlib

HOST = "127.0.0.1"
user = input("Enter your remote account: ")
password = getpass.getpass()

# Establish the connection
tn = telnetlib.Telnet(HOST)

# Wait for the username prompt and send the encoded username
tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")

# Wait for the password prompt and send the encoded password
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Execute a system command
tn.write(b"ls\n")
tn.write(b"exit\n")

# Read and print the entire terminal output
print(tn.read_all().decode('ascii'))
