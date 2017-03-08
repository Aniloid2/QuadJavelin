import time

ts = time.time()

temp_line = ''
for item in range(9600):
	
	b = open('data.txt', 'r')

	line = b.readline()


	b.close()
	if line != temp_line:
		temp_line = line
		print line

	to = (time.time() - ts)
	time.sleep(0.04)
	
print to
