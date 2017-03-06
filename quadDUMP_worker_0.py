import requests 
import json
import time

import sys

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
# client = requests.session()


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


user_inputs = sys.argv

quadname = user_inputs[1]
password = user_inputs[2]
time_delay = float(user_inputs[3])


print (quadname + password + str(time_delay))

time.sleep(time_delay)

#for testing 

# quadname = 'greg7'


URL = 'https://quadlink-c80dc.firebaseio.com/'+ quadname +'.json'
s = requests.Session()

print (URL)

payload = {
	'x_axis': 0,
	'y_axis': 0,
	'z_axis': 0,
}


t2 = time.time()
for item in range(1,100,1):
	
	payload['x_axis'] = item
	payload['y_axis'] = item
	payload['z_axis'] = item

	#print (payload)
	#ts = time.time()
	try:
	
		r = s.patch(URL, data=json.dumps(payload), timeout=0.2)
	except Exception as e:
		#print ('request has timed out: '+ str(e) +'\n')
		pass
	#ta = time.time()
	#dt = ta - ts
	#print ('Time before timeout' + str(0.2-dt)+'\n')
	#print ('Time difference:' + str(dt) + '\n')

print ('TIME2 '+ str(time.time() - t2))