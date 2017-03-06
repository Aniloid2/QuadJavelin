import requests
import time
# from hyper.contrib import HTTP20Adapter
# from hyper import HTTPConnection
import http.client

# s = requests.Session()
# s.mount('https://www.google.com', HTTP20Adapter())
# q = requests.Session()
c = http.client.HTTPConnection("quadlink-c80dc.firebaseio.com",80)

# q.mount('https://quadlink-c80dc.firebaseio.com/ferrari.json',HTTP20Adapter())



for i in range(4):

	ts = time.time()
	# r = s.get('https://google.com')
	# qd = q.get('https://quadlink-c80dc.firebaseio.com/ferrari.json')
	c.request("GET","/ferrari.json")


	print ('Time' + str((time.time() - ts)))
	#print (qd.text)
	res = c.getresponse()
	print (res.read())


# mount with www
# do requests with no www, always include https

# https://quadlink-c80dc.firebaseio.com/
