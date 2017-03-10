import numpy as np
import cv2
from PIL import Image
import binascii
import io
from scipy.ndimage import filters
import requests
import json
import time
import zlib




def unpack(newL):
	counter = 0
	for item in newL:
		#print 'we are at:', counter, 'the thing is', item, 'size', len(item)
		counter +=1
	#flattened = newL.flatten()
	a = flattened.tolist()
	#print a, 'donse', len(a)
	#print a
	return a
		








cap = cv2.VideoCapture(0)
cap.set(4,160)
cap.set(3,120)


URL = 'https://quadlink-c80dc.firebaseio.com/ferrari2.json'

# cap.set(4,1024)
# cap.set(3,1280)
payload ={
	'image':0
}
u = True
while True:

	if u == True:
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',gray)


		frame_bits = np.unpackbits(gray)
		print 'Before compression:', len(frame_bits)

		imx = np.zeros(gray.shape)
		#print len(imx)
		filters.sobel(gray,1,imx, mode='wrap')

		imy = np.zeros(gray.shape)
		filters.sobel(gray,1,imy, mode='wrap')

		magnitude = np.sqrt(imx**2+imy**2)

		#tipe of arrays
		print (magnitude.dtype, gray.dtype)
		#net the tipe to uint
		new = magnitude.astype(dtype = 'uint8')
		print (new.dtype)
		#make it into bits to see how big
		bite_size = np.unpackbits(new)
		print len(bite_size)
		#invert to have black lines
		newL = np.invert(new, dtype='uint8')
		print 'newL', newL

		a = unpack(gray)






		payload['image'] = a
		td = time.time()
		dump = json.dumps(payload)
		print 'time dump', (time.time() - td)
		ts = time.time()

		#r = requests.delete(URL)
		r = requests.patch(URL, data=dump)
		print 'time:', (time.time() - ts)
		#compress by raw
		frame_compressed = zlib.compress(newL,1)
		frame_compressed_from_bits = zlib.compress(np.unpackbits(newL),1)
		print len(frame_compressed), len(frame_compressed_from_bits)
		#better to compress pizle data


		uncompressed_frame = zlib.decompress(frame_compressed)

		print len(uncompressed_frame)

		# print frame_compressed
		print uncompressed_frame


		

		cv2.imshow('frame',gray)

		#print (magnitude)

		#print 'bits of bad image', solbersize

		# frame_compressed = zlib.compress(frame_bits,1)

		# print len(frame_compressed)

		# uncompressed_frame = zlib.decompress(frame_compressed)

		# print 'After Compression: ', len(uncompressed_frame)

		# hexi = binascii.hexlify(uncompressed_frame)
		# hexi = str(hexi)

		# im = Image.frombytes('L', (240, 320), hexi)
		u = True


		


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break




# value = "0110100001100101011011000110110001101111"

# carr = np.array([(255,255,255), (0,0,0)], dtype='uint8')
# data = carr[np.array(map(int, list(value)))].reshape(-1, 8, 3)
# img = Image.fromarray(data, 'RGB')