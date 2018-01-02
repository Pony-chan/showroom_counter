#########################################
# Auto count for showroom  1.0 created by Ponytail #
#########################################

#!/usr/bin/python

import time
import socket
import urllib

room_id = raw_input("Room ID: ")
url = "https://www.showroom-live.com/" + room_id

room = urllib.urlopen(url)

print(room)

print ("Counting...\nPress CTRL + C to stop")

for i in range(51):
	time.sleep(1.5);
	