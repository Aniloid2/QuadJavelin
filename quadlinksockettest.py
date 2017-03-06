import socket
import ssl
import time
import requests

# https://quadlink-c80dc.firebaseio.com/


HOST = 'quadlink-c80dc.firebaseio.com'                 # Symbolic name meaning all available interfaces
PORT = 443         # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    ss = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    ss.connect((HOST, PORT))
    for i in range(1):
    	ts = time.time()   	
    	request = "GET /ferrari.json HTTP/1.1\r\nHost: "+ HOST + "\r\nConnection: keep-alive\r\n\r\n"
    	ss.send(request.encode())
    	result = ss.recv(4096)
    	#print (result)
    	while (len(result)>0):
    		print (result)
    		result = ss.recv(4096)
    	print ('Time '+ str(time.time()-ts))



