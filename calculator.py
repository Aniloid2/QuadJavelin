import sys
import re

#Script used to calculate the total refresh rate

requ = open('sent_requ.txt', 'r')
refresh_rate = open('refresh_rate.txt', 'r')

topR = requ.readline().split(',')
bottomR = refresh_rate.readline().split(',')
topMin = topR[:-1]
bottomMin = bottomR[:-1]

# Python list creators, very efficient way to create lists in Python.
topMin = [float(x) for x in topMin]
bottomMin = [float(x) for x in bottomMin]

print  bottomMin, topMin



avrb = sum(bottomMin)/len(bottomMin)
avrt = sum(topMin)


refresh = avrt/avrb
print (refresh)

result = open('result.txt', 'a')
result.write('test carried out with 1 thread: ' + str(refresh)+ '\n')
result.close()

a = open('sent_requ.txt', 'w').close()
b = open('refresh_rate.txt', 'w').close()
