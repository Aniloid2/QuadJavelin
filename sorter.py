import serial
import time
import re

import sys

#This script reads characted by charecter coming from the serial port at
#a 9600 baud rate. This script is 1000 times faster than the fetcher.
#which means it can place the most upto date value for every fetcher with no
#issues.


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


	ignore = False
	

	#Logic bomb


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
				print coms_tog

				#file is oppened, priveous values are deleted and most up to date
				#ones entered

				multiplex = open('multiplex.txt', 'w')
				multiplex.write(coms_tog)
				multiplex.close()


				#For Debugging purposes, append to a text file the values from the serial port, 
				#join them with the time when values happened.
				# log = open('logging.txt', 'a')
				# time = time.strftime("%H:%M:%S", time.gmtime(666))
				# to_write = str(coms_tog) + str(time)
				# log.write(to_write)
				# log.close()


			while (len(coms)>0):
					coms.pop()
