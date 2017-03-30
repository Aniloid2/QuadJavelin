import requests 
import json
import time
import re
import sys
import random
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()



#This section of code is responsible with fireing the requests
#to the firebase server. testing can be set to true for debugging 
#purposes. The URL is the HTTP address of the noMySQL server.
#Originaly an object was going to be used to store the payload,
#however a simple dictionary proved more than fine. If this part of
#code was going to get more complicated than i would store the payload
#in an object.


testing = True


user_inputs = sys.argv
if testing == False:
	quadname = user_inputs[1]
	password = user_inputs[2]
	time_delay = float(user_inputs[3])
	ipaddress_phone = user_inputs[4]
	time.sleep(10)
	time.sleep(time_delay)

else:
	quadname = 'hector2'
	ipaddress_phone ='10.9.132.188:8080'

URL = 'https://quadlink-c80dc.firebaseio.com/'+ quadname +'.json'

#By creating a session i was able to mantain the 3 way handshake. this
#cuts the original 600ms individual requests to 120ms.
s = requests.Session()

print (URL)






payload = {
	'axis': {
	'pitch': 0,
	'roll': 0,
	'yaw': 0,
	},
	
	'acceleration': {
		'x_acc': 0,
		'x_acc': 0,
		'z_acc': 0,
		},

	# 'temp':0,
	'ip_address' : 0,
	'thrust' : 0,
}
count = 0
send = False
temp_line = ''

ta = time.time()
for item in range(100):
# while True:
	

	#serial can only be operated by one python script at the time.
	#this means my threads would have been useless. To solve this 
	#problem a sorter script that places the latest
	#value in a text file was implemented. Another option was to use
	#a SQLlite DB, however the time.time() function showed a text file
	#takes 0.0001s to open, compared to 0.9s for the DB. since the 
	#fetcher scripts take 200ms to compleate the sorter script is able to place
	#1000 serial values in the text file before a fetcher can grab another.
	
	if testing == False:
		multiplex = open('multiplex.txt', 'r')
		data_line = multiplex.readline()
		multiplex.close()
	else:
		data_line = ''
		payload = {
		'axis': {
			'pitch': random.randint(1,90),
			'roll': random.randint(1,90),
			'yaw': random.randint(1,90),
		},
		'acceleration': {
			'x_acc': random.randint(1,90),
			'y_acc': random.randint(1,90),
			'z_acc': random.randint(1,90),
			},
		# 'temp':item/10.0,
		'ip_address' : ipaddress_phone,
		'thrust':random.randint(1000,2000),
		}
		send = True


	


	
	time.sleep(0.04)
	#try not to waste request bandwith by sending same values 
	if data_line != temp_line:
		temp_line = data_line

		coms_spit = data_line.split(",")
		
		try:

			payload['axis']['pitch'] = coms_spit[0]

			payload['axis']['roll'] = coms_spit[1]

			payload['axis']['yaw'] = coms_spit[2]

			payload['acceleration']['x_acc'] = coms_spit[3]

			payload['acceleration']['y_acc'] = coms_spit[4]

			payload['acceleration']['z_acc'] = coms_spit[5]

			payload['ip_address'] = ipaddress_phone

			payload['thrust'] = coms_spit[6]

			send = True

			#if any entery in the payload in not entered (because the txt file is missing it)
			#then the script fails. no nead to send a request with a missing value.
			#the script imideatley starts the loop again, fetching the latest falues.
		except Exception as Ex:
			send = False
			print (Ex)

	#print payload

	if send:
		try:
			# The request
			ts = time.time()
			r = s.patch(URL, data=json.dumps(payload))
			to = time.time() - ts

			# For testing purposes, append latency to then calculate average
			# test_latency = open('latency_average.txt', 'a')
			# test_latency.write(str(to) + '+')
			# test_latency.close()


			# the 200ms timeout is still a problem, sometimes the request gets stuck
			# and results in the timeout, the session has to be reistablised and another 
			# request sent. this means when a timeout happens 900ms to 1s is wasted.
			print ('Time Taken For Req:' + str(to))
		except Exception as e:
			count = count + 1
			print ('request has timed out: '+ str(e) +'\n')
			pass


tf = time.time() - ta
print (count)

#for testing purposes, total time for number of requests
# refresh_rate = open('refresh_rate.txt', 'a')
# maths = tf
# refresh_rate.write(str(maths) + ',' )
# refresh_rate.close()

# requ = open('sent_requ.txt', 'a')
# requ.write(str(200-count) + ',')
# requ.close()





