import socket

remoteServer = "localhost"

remoteServerIP = socket.gethostbyname(remoteServer)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = sock.connect_ex((remoteServerIP, 8000))


if result == 0:
	print "port is open"



print "response = " +str(result)

sock.close()