import socket
import os
import time

host = socket.gethostname()
port = 3141

while True:
    os.system("gphoto2 --capture-image-and-download --filename ./images/image_to_send.jpg --force-overwrite")

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('192.168.0.139', port))

    with open("./images/image_to_send.jpg", 'rb') as file_to_send:
        for data in file_to_send:
            clientsocket.sendall(data)
        file_to_send.close()

    clientsocket.close()
    time.sleep(1)
