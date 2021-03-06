import socket
import datetime

# Test filed downloaded from https://speed.hetzner.de/

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostbyname('raspberrypi')

port = 3141

clientsocket.connect(('192.168.0.139', port))

filename = "./testfiles/100MB.bin"
recievedSpeed = False
clientsocket.send(filename.encode('ascii'))
first = True
hold = b''
with open("./testfiles/100MB_dl.bin", 'wb') as file_to_write:
	while True:
		data = clientsocket.recv(1024)
		if not data:
			break
#		file_to_write.write(data)
		hold = data
	file_to_write.close()
speed = hold.decode('ascii')

print('Download Speed: ', speed, "MB/s")

clientsocket.close()
