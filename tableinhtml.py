import socket
import datetime
import os
import commands
import HTML


def get_cpu_temp_celsius():
    	tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    	cpu_temp = tempFile.read()
    	tempFile.close()
    	return float(cpu_temp)/1000

HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print 'Serving HTTP on PORT %s ...' % PORT

while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	print request


	http_status = "HTTP/1.1 200 OK \n"
	http_type = "Content-type: text/html\n"

	table_data = [

	['Smith',	'John',	30],
	['Carpenter',	'Jack',	45],
	['Johnson',	'Paul',	62],
	
	]


	http_body = """
	
	<html>

	<head>
		<title>Statistics</title>
	</head>
		<body>
	<center><b>Device Statistics</b></center>
	<div id="holder" style="width:600px; height:300px">
	<p>
	The CPU Temperature is
	""" + str(get_cpu_temp_celsius())+"""</p>
	<p>
	The load Average is
	""" + str(os.getloadavg()) +"""</p>
	<p>
	""" + HTML.table(table_data,header_row=['Lastname', 'First name', 'Age']) + """</p>
	</div>
		</body>


	</html>


	"""




	client_connection.send(http_status)
	client_connection.send(http_type)
	client_connection.send(http_body)
	client_connection.close()