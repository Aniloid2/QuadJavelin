import serial


serialport = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)


coms = []
allready_happended = False
add = False
brake = False
counter = 0
while True:   
	

	command = str(serialport.read(1))
	print command
	#print counter 
	counter += 1

	if command == "-":
		if (len(coms) == 0):
			add = True 
		if (len(coms) >= 12):
			print 'Im big'
			brake = True
			add = False

	if add == True:
		if command == "-":
			pass
		else:
			#print command
			coms.append(command)

	if brake == True:
		#use this
		print coms
		for item in coms:
			del item	
		# if counter%1000 == 0:
		# 	print counter
		brake == False
		add == True












	# if allready_happended = False:
	# 	if command == "-":
	# 		print 'begin coms'
	# 		allready_happended = True

	# 	if command != "-":
	# 		coms.append(command)

	# if command != "-":
	# 	coms.append(command)
	# else:
	# 	allready_happended = False






	# if command == "-":
	# 	if happended == True:
	# 		pass
	# 	else:
	# 		happended = True

	# if happended == True:	
	# 	# if (len(coms) == 0) & (command == "-"):
	# 	# 	print 'just dash'
	# 	# 	pass

	# 	if ((len(coms) <= 12) & (command != "-")):
	# 		coms.append(command)
	# 		print 'keep adding'

	# 	else:
	# 		if command == "-":
	# 			print 'coms stopped'
	# 			#do someting with array
	# 			for item in coms:
	# 				del item
	# 		else:
	# 			print 'add risk'
	# 			coms.append(command)

 # 	print coms

	# Com3string = Com3.readline()
	# Com3splitted = Com3string.split(",")
	# print Com3splitted


