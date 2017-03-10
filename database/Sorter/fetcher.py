import requests 
import json
import time
import re
import sys

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


def calculate_gx(ax):
	gf = ax/16384.0
	accelerationx = gf * 9.81

def calculate_gy(ay):
	gf = ay/16384.0
	accelerationy = gf * 9.81




user_inputs = sys.argv

quadname = user_inputs[1]
password = user_inputs[2]
time_delay = float(user_inputs[3])

URL = 'https://quadlink-c80dc.firebaseio.com/'+ quadname +'.json'
s = requests.Session()

print (URL)



time.sleep(time_delay)


payload = {
	'pitch': 0,
	'roll': 0,
	'yaw': 0,
	'temp':0,
	'x_acc':0,
	'x_acc':0,
	'z_acc':0,
}


temp_line = ''
for item in range(100):
	

	multiplex = open('multiplex.txt', 'r')

	data_line = multiplex.readline()


	multiplex.close()
	time.sleep(0.04)

	## calculate_g()

	#try not to waste request bandwith by sending same values 
	if data_line != temp_line:
		temp_line = data_line

		coms_spit = data_line.split(",")
		
		try:
			# try:
			payload['pitch'] = coms_spit[0]
			# except Exception as P:
			# 	print (P)
			# try:
			payload['roll'] = coms_spit[1]
			# except Exception as R:
			# 	print (R)
			# try:
			payload['yaw'] = coms_spit[2]
			# except Exception as Y:
			# 	print (Y)
			# try:
			payload['temp'] = coms_spit[3]
			# except Exception as T:
			# 	print (T)

			# try:
			payload['x_acc'] = coms_spit[4]
			# except Exception as AX:
			# 	print (AX)

			# try:
			payload['y_acc'] = coms_spit[5]
			# except Exception as AY:
			# 	print (AY)

			# try:
			payload['z_acc'] = coms_spit[6]
			# except Exception as AZ:
			# 	print (AZ
			send = True
		except Exception as Ex:
			send = False
			print (Ex)


		print data_line

		if send:
			try:
				# ts = time.time()
				r = s.patch(URL, data=json.dumps(payload), timeout=0.2)
				# to = time.time() - ts
				#print ('Time Taken For Req:' + str(to))
			except Exception as e:
				print ('request has timed out: '+ str(e) +'\n')
				pass



	
