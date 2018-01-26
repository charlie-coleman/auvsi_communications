import socket
import datetime
import time

# Test filed downloaded from https://speed.hetzner.de/

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = socket.gethostname()

port = 3141

serversocket.bind(('', port))

serversocket.listen(5)
while True:
	clientsocket,addr = serversocket.accept()

	startTime = datetime.datetime.utcnow()

	reqFile = clientsocket.recv(1024)

	with open(reqFile, 'rb') as file_to_send:
		for data in file_to_send:
			clientsocket.sendall(data)

	endTime = datetime.datetime.utcnow()

	totalTime = endTime-startTime

	speed = 100.0 / totalTime.total_seconds()
	speedstr = str(speed).encode('ascii')
	print("Upload Speed: ", speedstr.decode('ascii'), "MB/s")

	time.sleep(1)
	clientsocket.send(speedstr)
	clientsocket.close();
