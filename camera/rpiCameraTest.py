import os
import datetime

while True:
	os.system('gphoto2 --capture-image-and-download -F 5 -I 1 --no-keep --force-overwrite --filename "./images/pic-%Y%m%d-%H:%M:%S.jpg"');
