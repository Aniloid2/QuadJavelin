import serial
import requests 
import json
import time
import re
from subprocess import Popen

import sys

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

serialport = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)



quadname = 'ferrari'
URL = 'https://quadlink-c80dc.firebaseio.com/'+ quadname +'.json'
s = requests.Session()

print (URL)

payload = {
	'pitch': 0,
	'roll': 0,
	'yaw': 0,
}


coms = []
begining = False
end = False
ignore = True
count = 0
while True:

	command = str(serialport.read(1))
	#print command
	ts = time.time()
	tr = time.time()


	if command == "-":
		ignore = True
	else:
		ignore = False

	if ignore == False:
		if command == "[":
			begining = True
			end = False
		elif command ==")":
			end = True
			begining = False

		if begining == True:
			if command != "[":
				coms.append(command)


		#its entering every time a new array is created,
		if end == True:

			count += 1
			if command == ")":
				
				#print ('use this')
				coms_tog = "".join(coms)
				coms_spit = coms_tog.split(",")
				try:
					payload['pitch'] = coms_spit[0]
				except Exception as P:
					print (P)
				try:
					payload['roll'] = coms_spit[1]
				except Exception as R:
					print (R)
				try:
					payload['yaw'] = coms_spit[2]
				except Exception as Y:
					print (Y)

				print payload
				print ('time to list' + str(time.time() - tr))
				#ts = time.time()
				try:
					print payload

					#time.sleep(0.2)
					print count
					if count%35 == 0: # 35 faster refresh rate worst latency, 50 better latency but worst refresh rate. 
						#print ('--------------------------sending request-------------------------------')
						r = s.patch(URL, data=json.dumps(payload), timeout=0.2)
						#print ('---------------------------donse sending--------------------------------')
					else:
						pass

					#r = s.patch(URL, data=json.dumps(payload), timeout=0.2)

				except Exception as e:
					print ('request has timed out: '+ str(e) +'\n')
					pass
				ta = time.time()
				dt = ta - ts
				print ('Time difference: ' + str(dt))
				dlt = time.time()
				while (len(coms)>0):
					coms.pop()
				dlt_af = time.time()
				print ('Time delete:' + str(time.time() - dlt_af))
					
