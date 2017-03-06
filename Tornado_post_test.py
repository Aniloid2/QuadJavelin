

#import requests 
import json
import time
from urllib3 import HTTPConnectionPool
import sys


quadname = ('ferrari')
URL = 'https://quadlink-c80dc.firebaseio.com/'+ quadname +'.json'
s = HTTPConnectionPool(host='quadlink-c80dc.firebaseio.com', port=443, maxsize=1)

print (URL)

payload = {
	'x_axis': 0,
	'y_axis': 0,
	'z_axis': 0,
}


t2 = time.time()
for item in range(1,6,1):
	
	payload['x_axis'] = item
	payload['y_axis'] = item
	payload['z_axis'] = item

	#print (payload)
	ts = time.time()
	try:
	
		r = s.request('PATCH','/ferrari.json',fields = {'x_axis':90})
	except Exception as e:
		#print ('request has timed out: '+ str(e) +'\n')
		print (e)
		pass
	ta = time.time()
	dt = ta - ts
	print (r)
	#print ('Time before timeout' + str(0.2-dt)+'\n')
	print ('Time difference:' + str(dt) + '\n')

print ('TIME2 '+ str(time.time() - t2))