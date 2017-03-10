import numpy as np

import zlib, base64


text = np.array([[2],[1]])
print text
tex_uni = text.astype(dtype='uint8')

tx = np.unpackbits(tex_uni)

print tx

compress =base64.b64encode(zlib.compress(tx))




un = zlib.decompress(base64.b64decode(compress))

for item in un:
	if item == 'Null':
		print '0'
	if item == 'SOH':
		print '1'
print un