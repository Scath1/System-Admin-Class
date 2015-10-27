import socket
import sys
import datetime


# Ask for input

remoteServer = "localhost"
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a nice banner with informatin on which to host we are about to scan

print "-" * 60

print "Please wait, scanning a remote host", remoteServerIP

print "-" * 60


for port in range (1, 1025):
	

# We also put in some error handling for catching errors


	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print "Port {}: \t Open".format(port)
		sock.close()


	except socket.gaierror:
		print "hostname could not be resolved. Exiting"
		sys.exit

	except socket.error:
		print "couldnt connect to server"
		sys.exit()