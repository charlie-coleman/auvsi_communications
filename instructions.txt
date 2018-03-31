SPEEDTEST:
--------------------------
1. Navigate to ~/auvsi_communications/speedtest on the RPi
2. Run "sh ./server.sh"
	Keep the ssh open to make sure nothing crashes
3. git clone https://github.com/charlie-coleman/auvsi_communications.git
   if you haven't done so already somewhere on the PC acting as server
4. Navigate to auvsi_communications/speedtest on the PC
5. Run "sh ./client.sh N" where N is the number of speed test trials you want to do.
6. Record output

CAMERA:
--------------------------
1. Navigate to ~/auvsi_communications/camera on the RPi
2. Run "python3 rpiCameraTest.py"
3. Camera should continuously takes picture, about every 3 seconds
4. To stop the pictures, hit Ctrl+Z or unplug the camera


The SSH password should be raspberry

