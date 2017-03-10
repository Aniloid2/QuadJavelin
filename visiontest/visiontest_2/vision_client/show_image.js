function show_img(lissener_obj) {

	var doc_thing = document.getElementById('doc_thing');
	console.log(inside)

	var Uint_array = function(doc_thing, fire_array) {

		var to_return_array = [];
		var color_array=[];
		var ctx = doc_thing.getContext('2d');

		//dosn't work
		// var to_return_array = new Uint8ClampedArray(19200)
		// var ctx = doc_thing.getContext('2d');
		// console.log('initial size', to_return_array.length)
		// for (var i = 0; i <= fire_array.length-1; i++) {
		// 	console.log('iteration', i)
		// 	var u8fire = Uint8ClampedArray.from(fire_array[i])
		// 	console.log(u8fire)
		// 	to_return_array[i] = u8fire
		// 	console.log(to_return_array)

			// ctx.putImageData(u8fire, 20,20);

		//second try
		//first array for gray

		for (var i = 0; i < fire_array.length; i++) {
			to_return_array = to_return_array.concat(fire_array[i]);

		};

		// console.log(to_return_array, to_return_array.length )

		//second array for gray
		// for (var i=0; i<to_return_array.length; i++) {
		// 	console.log(i, color_array.length)
		// 	color_array = color_array.concat(to_return_array[i])
		// }


		var last = Uint8ClampedArray.from(to_return_array)
		console.log('array cheat', last)

		// //
		// var color = Uint8ClampedArray.from(color_array)
		// console.log('array color', color)

		//streight all in one line
		// var faster = Uint8ClampedArray.from(fire_array)
		// console.log('array color', faster)


		ctx.scale(3,1)
		img = new ImageData(last, 44)
		// col_img = new ImageData(color,96)
		// fast = new ImageData(faster, 44)

		
		ctx.putImageData(img,2,2);

		// ctx.putImageData(col_img, 50,50)

		// ctx.putImageData(fast, 2,2)
		

		console.log(doc_thing)
		return to_return_array

	}

	lissener_obj.imageU.on('value' , function(snapshot) {
		console.log('about to enter')
		Uint_array(doc_thing, snapshot.val())
	})

	console.log('returned array', Uint_array)



}