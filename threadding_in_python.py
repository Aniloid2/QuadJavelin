from multiprocessing import Pool, TimeoutError

import requests 
import time
import json

import grequests

payload = {
	'x_axis': 1,
	'y_axis': 1,
	'z_axis': 1,
}

payload2 = {
	'x_axis': 5,
	'y_axis': 5,
	'z_axis': 5,
}

payload3 = {
	'x_axis': 3,
	'y_axis': 3,
	'z_axis': 3,
}



list1 = [payload, payload2, payload3]



def f(x):
	with requests.Session() as s:
		r = s.patch('https://quadlink-c80dc.firebaseio.com/greg7.json', data=json.dumps(x))

def main():

	print (list1)

	ts = time.time()

	with Pool(8) as pool:
		pool.map_async(f,list1)
		time.sleep(2)
		print ('Took {}s'.format(time.time() - ts))



if __name__ == '__main__':
	while True:
		main()
		print ('hi')
    # for i in range (4):
    # 	pool = Pool(processes = 1)
    # 	res = pool.apply_async(f, (i,i,i))
    # 	print res.get(timeout=2)