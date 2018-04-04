import sys
import socket
import datetime

# Test filed downloaded from https://speed.hetzner.de/

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = socket.gethostname()
if (len(sys.argv) > 0):
    port = int(sys.argv[1])
else:
    port = 3141

serversocket.bind(('0.0.0.0', port))

serversocket.listen(5)
try:
    while True:
        clientsocket,addr = serversocket.accept()

        print("Recieved connection, downloading image")
        filename = "./images/image_"+datetime.datetime.now().strftime("%Y%m%d_%H:%M:%S")+".jpg"

        with open(filename, 'wb') as file_to_write:
            while True:
                data = clientsocket.recv(1024)
                if not data:
                    break
                file_to_write.write(data)
            file_to_write.close()
        print('Download Completed')
        clientsocket.close()
except KeyboardInterrupt:
    print('Interrupted')
    serversocket.close()
