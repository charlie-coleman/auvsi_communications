import socket
import datetime

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 3142

clientsocket.connect((host, port))

filename = "./64MB.dat"
recievedSpeed = False
clientsocket.send(filename.encode('ascii'))
with open("./64_dl.dat", 'wb') as file_to_write:
	while True:
		data = clientsocket.recv(1024)
		if not data:
			break
		file_to_write.write(data)
	file_to_write.close()

while True:
	data = clientsocket.recv(1024)
	if not data and recievedSpeed:
		break
	if data:
		recievedSpeed = True
		print(data.decode('ascii'))
clientsocket.close()
