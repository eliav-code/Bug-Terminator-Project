from bug_color_detection import *
#from regular_move import *
#from test1 import Drive
#import cv2
import time
import socket
import urllib
import cv2
import numpy as np
import requests


camip="http://192.168.43.21:8080/"    # You have to put the specific ip address and port.
class Car:

    def __init__(self):

        #capture = cv2.VideoCapture(0)
		# The camera start a streaming
	global camip
        count=0
        stream = urllib.urlopen(camip+"stream.mjpg")
        bytes = ''
        while True:


			bytes += stream.read(1024)
			a = bytes.find('\xff\xd8')
			b = bytes.find('\xff\xd9')
			if a == -1 or b == -1:
				continue
			jpg = bytes[a:b+2]
			bytes = bytes[b+2:]
			image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
			height,width = image.shape[:2]
			if(count==2):
				count=0
				okay=True
			else:
				count+=1
				okay=False

			part = 0.1                                   # The percent of the screen to use
			min_dis_x = part * width                     # min distance needed from middle x
			#min_dis_y = part*2 * height                  # min distance needed from bottom of the screen
														  # TODO check if getting closer is moving it to the bottom otherwise continue as usual.
			middle = (width/2, height/2)

			if okay:
				pos = track(image)                   # Call function that find bug
				if pos is None:
					return
				if pos != (-1, -1):                  # If bug found
					dist = abs(middle[0]-pos[0])     # X distance
					if dist <= min_dis_x:            # In the middle x
						dist_y = abs(height-pos[1])  # Distance from the bottom of the screen
						if dist_y <= height*0.15:    # TODO maybe we need to use an ultra sonic
							requests.post(camip,"Trigger")						 #my_socket.send('Trigger water gun')
													 								# TODO Here we will need to trigger on the spray and squirt on the bug.
						else:
							requests.post(camip, "M_F")# If not at bottom move to bottom
					else:
						if middle[0] > pos[0]:   # If middle is larger than posX, the meaning is - I need to go left.
							requests.post(camip,"RO_L")#my_socket.send('Rotate left')
						else:
							requests.post(camip,"RO_R")		#my_socket.send('Rotate right')  # The opposite of three lines before

				else:
					requests.post(camip,"R_M")		#my_socket.send('Regular move')  	# TODO call the regular function who drives before finds a bug.
			if cv2.waitKey(1) & 0xFF == ord('q'):

				break



Car()

