import os
import datetime
import _thread
import time
import socket
import sys

host = socket.gethostname()
if (len(sys.argv) > 0):
    port = sys.argv[0]
else:
    port = 3141

def download_thread(lfs):
    try:
    	while True:
    		files = [f for f in os.listdir('./images') if os.path.isfile('./images/'+f)]
    		if len(files) < 1:
    			time.sleep(0.5)
    			continue
    		files.sort()
    		file_to_send = files[0]
    		print("SENDING: " + file_to_send)
    		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    		clientsocket.connect(('192.168.0.139', port))

    		with open("./images/"+file_to_send, 'rb') as file_being_sent:
    			for data in file_being_sent:
    				clientsocket.sendall(data)
    			file_being_sent.close()
    		print("FILE SENT")
    		os.system("mv ./images/"+file_to_send+" ./images/sent/"+file_to_send)
    		clientsocket.close()
    		time.sleep(0.5)
    except KeyboardInterrupt:
def input_thread(a_list):
	input()
	a_list.append(True)

a_list = []
last_file_sent = '';
_thread.start_new_thread(input_thread, (a_list,))
_thread.start_new_thread(download_thread, (last_file_sent,))
while not a_list:
	os.system('gphoto2 --capture-image-and-download -q -F 4 -I 1 --no-keep --force-overwrite --filename "./images/pic-%Y%m%d-%H:%M:%S.jpg"')
