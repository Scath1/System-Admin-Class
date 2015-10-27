import socket

hostname = str(raw_input("Enter an IP address "))

hostIP = socket.getfqdn(hostname)

print hostIP