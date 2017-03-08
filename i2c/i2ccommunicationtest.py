
import smbus

bus=smbus.SMBus(1)



DEVICE_ADDRESS = 0x51 ## depends on jays choice
D = 0x68

DEVICE_REG_MODE = 0x00 # no idea what it is cmd



def readNumber(a):

	# try:
	# 	number = a.read_byte(DEVICE_ADDRESS)
	# 	print number 
	# 	return number
	# except Exception as e:
	# 	print e

	try:
		number2 = a.read_i2c_block_data(D, DEVICE_REG_MODE)
		print (number2)
		return number2
	except Exception as b:
		print b
	
	

while True:
 	number_recived1 = readNumber(bus)
 	print (number_recived1)