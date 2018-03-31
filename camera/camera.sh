python3 groundstation.py &

sshpass -p "auvsirpi" ssh pi@raspberrypi -- "cd ~/auvsi_communications/camera && python3 rpi.py"
