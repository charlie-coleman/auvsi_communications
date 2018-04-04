python3 groundstation.py 7654 &

sshpass -p "auvsirpi" ssh pi@raspberrypi -- "cd ~/auvsi_communications/camera && python3 rpi.py 7654"
