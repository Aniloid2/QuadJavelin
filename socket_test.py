# create an INET, STREAMing socket

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # now connect to the web server on port 80 - the normal http port
# server ='www.python.org'

# requests = "GET / \nHost: "+ server+"\n\n"
# s.connect((server, 443))



# a = s.send(requests.encode())

# result = s.recv(4096)
# print (result)

import socket
import ssl
import time
import requests

HOST = 'pythonprogramming.net'                 # Symbolic name meaning all available interfaces
PORT = 443         # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    ss = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    ss.connect((HOST, PORT))
    for i in range(1):
    	ts = time.time()   	
    	request = "GET /data-analysis-python-pandas-tutorial-introduction/ \nHost: "+ HOST+"\n\n"
    	ss.send(request.encode())
    	result = ss.recv(4096)
    	#print (result)
    	while (len(result)>0):
    		print (result)
    		result = ss.recv(4096)
    	print ('Time '+ str(time.time()-ts))



