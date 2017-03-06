import requests 
import json
import time

from json_tricks import dump, dumps

import sys

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
# client = requests.session()

import numpy as np
import cv2

import zlib

cap = cv2.VideoCapture(0)


#for reading from bus, talk to jay, will he store values
#in register? if so i can do the folowing

#

# install python-smbus

# import smbus

class I2Cinput(object):
	"""docstring for I2Cinput"""
	def __init__(self, number_recived1, number_recived2):
		self.x_axis = number_recived1
		self.y_axis = number_recived2
		
		


# bus=smbus.SMBus(1)

# DEVICE_ADDRESS = 0x15 ## depends on jays choice
# DEVICE_ADDRESS2 = 0x15 ## depends on jays choice

# DEVICE_REG_MODE = 0x00 # no idea what it is cmd


# def readNumber():
# 	number = bus.read_byte(DEVICE_ADDRESS)
# 	return number 

# def readNumber():
# 	number = bus.read_byte(DEVICE_ADDRESS2)
# 	return number 

# while True:
# 	number_recived1 = readNumber()
#   number_recived2 = readNumber2()
#	create object with recived data ===
#	current_ic2_input = I2Cinput(number_recived1, number_recived2)
#	?? have a function to host a worker, pass the current_ic2_input to worker
#   ?? json the passed variable in worker

# 	print (number_recived)


# user_inputs = sys.argv

# quadname = user_inputs[1]
# password = user_inputs[2]
# time_delay = float(user_inputs[3])


# print (quadname + password + str(time_delay))


#for testing 

quadname = 'ferrari'


URL = 'https://quadlink-c80dc.firebaseio.com/'+ quadname +'.json'
s = requests.Session()

print (URL)

payload = {
	'image':0,
	'x_axis': 0,
	'y_axis': 0,
	'z_axis': 0,
}


t2 = time.time()

while True:
	for item in range(1,2,1):
		
		payload['x_axis'] = item
		payload['y_axis'] = item
		payload['z_axis'] = item

		tIg = time.time()

		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',gray)

		C = time.time()
		frame_bits = np.unpackbits(frame)
		print (frame_bits)
		frame_compressed = zlib.compress(frame_bits,1)
		print (len(frame_compressed))
		print ('Timecompression' + str((time.time()-C)))

		payload['image'] = encoded_frame
		print ('Timeimage' + str((time.time()-tIg)))
		#print (payload)
		ts = time.time()
		try:

			r = s.patch(URL, data=json.dumps(payload))
		
		except Exception as e:
			print ('request has timed out: '+ str(e) +'\n')
			pass
		ta = time.time()
		dt = ta - ts
		print ('Time difference:' + str(dt) + '\n')

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break



print ('TIME2 '+ str(time.time() - t2))

cap.release()
cv2.destroyAllWindows()

