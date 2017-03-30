
import random
import time



# for left in range(100):
# 	time.sleep(0.2)
# 	multiplex = open('multiplex.txt', 'w').close()	
# 	random_integers = [ (str(random.randint(-100,100)) + ',') for i in range(7)]
# 	print (random_integers)
# 	multiplex = open('multiplex.txt', 'a')
# 	for item in random_integers:
# 		multiplex.write(item)
# 	multiplex.close()


for left in range(500):
	time.sleep(0.05)
	random_integers = [ str(random.randint(-100,100)) for i in range(7)]
	print (random_integers)
	multiplex = open('multiplex.txt', 'w')
	multiplex.write('{},{},{},{},{},{},{}'.format(random_integers[0],random_integers[1],random_integers[2],random_integers[3],random_integers[4],random_integers[5],random_integers[6]))
	multiplex.close()



