import socket
import datetime
import os
import commands
import HTML
import psutil

diskusage = psutil.disk_io_counters(perdisk=True)
netcon = psutil.net_io_counters(pernic=True)
sysmemory = psutil.virtual_memory()
CPUpercent = psutil.cpu_percent(interval=1)


remoteServer = "localhost"
remoteServerIP = socket.gethostbyname(remoteServer)

for port in range (1, 1024):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((remoteServerIP, port))
	if result == 0:
		print "Port {}: \t Open".format(port)
	sock.close()


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


	table_percentage = [

	['CPU Percentage',	str(CPUpercent)],
	['CPU Temperature',	str(get_cpu_temp_celsius())],
	['CPU Count',		str(psutil.cpu_count())],
	['CPU Times',		str(psutil.cpu_times())],
	
	]

	table_memory = [

	['System Memory Stats', 	str(sysmemory)],
	['Virtual Memory Percentage',	str(psutil.virtual_memory().percent)],
	['Disk Usage',			str(psutil.disk_io_counters(perdisk=True))],
	['Boot time',			str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))],
	['Device Name',		str(socket.gethostname())],

	]

	table_netstat = [

	['Packets Sent',	str(netcon['wlan0'].packets_sent)],
	['Packets Recieved',	str(netcon['wlan0'].packets_recv)],
	['Incoming Packets Dropped',	str(netcon['wlan0'].dropin)],
	['Outgoing Packets Dropped',	str(netcon['wlan0'].dropout)],
	
	]
	

	temptable = HTML.Table(header_row=['Temp',	'Result'])

	temp = get_cpu_temp_celsius()
	if temp > 70:
		color = 'Red'
		Result = 'Critically High'
	elif temp > 40:
		color = 'Yellow'
		Result = "Warning"
	else:
		color = "Green"
		Result = "Good"

	colored_result = HTML.TableCell(temp, bgcolor=color)
	html_percentage = HTML.Table(table_percentage)
	html_percentage.rows.append([temp, colored_result])


	HTML_COLORS = ['Black', 'Green', 'Silver', 'Lime', 'Gray', 'Olive', 'White', 'Maroon', 'Navy', 'Red', 'Blue', 'Purple', 'Teal', 'Fuchsia', 'Aqua']

	colortable = HTML.Table(header_row=['Name', 'Color'])

	for colorname in HTML_COLORS:
		colored_cell = HTML.TableCell(' ', bgcolor=colorname)
		colortable.rows.append([colorname, colored_cell])

	http_body = """
	
	<html>

	<head>
	
	<meta http-equiv="refresh"
	content="15">

	

	<style>

	#left {
	float:left;
	width:45%;
	margin-left:5px;
	vertical-align: top;
	}
	#right {
	width:45%;
	float:right;
	margin-right:5px;
	vertical-align: top;
	}


	h1 {
	text-align: center;
	}

	h2 {
	font-weight: 750;
	}
	h2 {
	text-decoration:
	underline;
	}

	
	
	</style>


		<title>Statistics</title>
	</head>
		<body>
	<h1>Device Statistics</h1>
	<div id="holder" style="width:1100px; height:310px">
	
	<div id="left">
	<h2>
	CPU Stats</h2>
	<p>
	""" + str(html_percentage) + """</p>
	</div>

	<di id="right">
	<h2>
	Network Stats </h2>
	<p>
	""" + HTML.table(table_netstat) + """ </p>
	</div>
	
	
	<h2>

	System Memory Information </h2>
	<p>
	""" + HTML.table(table_memory) + """ </p>
	
	
	
	
	</div>

	
		</body>


	</html>


	"""




	client_connection.send(http_status)
	client_connection.send(http_type)
	client_connection.send(http_body)
	client_connection.close()