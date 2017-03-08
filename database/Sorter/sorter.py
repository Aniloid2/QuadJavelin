import serial
import requests 
import json
import time
import re

import sys

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()



serialport = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)





coms = []
begining = False
end = False
ignore = True
count = 0
while True:

	command = str(serialport.read(1))

	#logic bomb
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
				print coms_spit
