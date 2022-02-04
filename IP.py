import socket
hostname = socket.gethostname()
IP= socket.gethostbyname(hostname)
print("Host_Name: "+hostname)
print("IP_ADDRESS: "+IP)
