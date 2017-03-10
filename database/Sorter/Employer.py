import sys
import os
import re



def delete_workers():
	cwd = os.getcwd()
	listed_directory_files = os.listdir(cwd)
	for file_ in listed_directory_files:
		if re.findall(r'worker',file_):
			print ("Deleting file:" + file_)
			os.remove(file_)

def check_errors(passed_args):
	print (passed_args)
	## if first argument is delete_all go to function that deletes all files in directory ecept
	#this one and the first quad dump
	if passed_args[1] == "-d":
		print ("~~ File remuval starting")
		delete_workers()
		print ("~~ All workers deleted")


	if (len(passed_args) == 4):
		print ('~~ File creation starting')			
		return True
	else:
		print ('~~ Enter 3 arguments, 1 = name of quad, 2 = password, 3 = refresh rate')
		print ('~~ Delete workers with -d extension')
		return False

def read_master_file():
		file_dump = open("fetcher.py", 'r')
		read_dump = file_dump.read()
		file_dump.close()
		return read_dump

def create_files(FPS, read_quaddump):
	for i in range(0,int(FPS),1):
		file_format = ("fetcher_worker_{}.py".format(i))
		print ('~~ Creating '+ file_format+ '...')
		file_create = open(file_format, 'w')
		file_create.write(read_quaddump)
		file_create.close()
		print ('~~ Done')


def create_bash_executable(FPS, Name,password):
	open("turn_on.sh", "w").close()
	print (open("turn_on.sh", "r").read())
	bash = open("turn_on.sh", "a")
	bash.write("python sorter.py & \n")
	for i in range(0,int(FPS),1):
		if i == 0:
			time_delay = i
		else:
			time_delay = i/10.0
		print (time_delay)
		name_executable = ("python fetcher_worker_{}.py {} {} {} & \n".format(i, Name,password, time_delay))
		bash.write(name_executable)

	bash.close()


def main(passed_args):
	Bool_door = False
	while True:
		while Bool_door == True:
			# Here Code Works, read file and duplicate for number of frames
			read_quaddump = read_master_file()
			FPS = passed_args[len(passed_args) - 1]
			Name = passed_args[len(passed_args)-3]
			password = passed_args[len(passed_args)-2]
			print ('~~ Hi '+ Name)
			create_files(FPS, read_quaddump)
			
			

			create_bash_executable(FPS, Name,password)
			print ('~~ Thank you for using us!')
			sys.exit()

		while Bool_door == False:
			Bool_door = check_errors(passed_args)
			if Bool_door == False:
				sys.exit()









if __name__ == '__main__':
	main(sys.argv)

# file_dump = open("quadDUMP.py", 'r')
# read_dump = file_dump.read()
# file_dump.close()


# file_create = open("quadDUMP2.py", 'w')
# file_create.write(read_dump)
# file_create.close()