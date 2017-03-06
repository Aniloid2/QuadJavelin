var imgd = context.createImageData(50,50);
var pix = imgd.data;

// Loop over each pixel and set a transparent red.
for (var i = 0; n = pix.length, i < n; i += 4) {
	pix[i  ] = 255; // red channel
	pix[i+3] = 127; // alpha channel
}

// Draw the ImageData object at the given (x,y) coordinates.
context.putImageData(imgd, 0,0);