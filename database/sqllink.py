import time

ts = time.time()
for item in range(9600):
	
	a = open('data.txt', 'w')

	n = a.write('{},{},{}\n'.format(item/3,item/6,item/7))
	print n
	a.close()
	to = (time.time() - ts)
	time.sleep(0.04)
	
print to

