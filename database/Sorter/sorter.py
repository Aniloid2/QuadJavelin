import serial
import time
import re

import sys


#initialise serial port 
serialport = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)




#logic control
coms = []
begining = False
end = False
ignore = True
count = 0
while True:

	#one character per while loop
	command = str(serialport.read(1))

	#print command

	#Logic bomb
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


		#Its entering every time a new array is created,
		if end == True:

			count += 1
			if command == ")":

				coms_tog = "".join(coms)
				#print 'adding'

				#Do stuff here
				#print coms_tog
				multiplex = open('multiplex.txt', 'w')
				multiplex.write(coms_tog)
				multiplex.close()


			while (len(coms)>0):
					coms.pop()
