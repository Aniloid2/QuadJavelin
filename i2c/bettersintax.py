import serial

serialport = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)



coms = []
begining = False
end = False
ignore = True
while True:

	command = str(serialport.read(1))
	#print command

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

		if end == True:
			if command == ")":
				#print coms
				#print ('use this')
				coms_tog = "".join(coms)
				print coms_tog
				while len(coms) > 0 : coms.pop()


# so at the moment we can only initialise one script. read data and post, same frequency as one and and delay is the same.
# addon sqllib in between 
# python script that takes inputs adds to sql and closes connection, then multiple scripts that open and close sql to read data.