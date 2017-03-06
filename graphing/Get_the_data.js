// window.onload = initAll;


function get_the_data() {
	var po = document.getElementById('po');
	console.log(po)

	var inside = document.getElementById('inside');
	console.log(inside)

	var up = function(element, val) {
		console.log(val)
		element.textContent = val;
	}

	var insidefun = function(element, val) {
		console.log(val)
		element.textContent = val;
	}


	console.log('hi');

	var quad = document.getElementById("quad_username").value;

	var databaseURL = "https://quadlink-c80dc.firebaseio.com"

	var folder = quad.concat(databaseURL)
	console.log(folder)


	console.log(quad)

	var config = {
	apiKey: "AIzaSyA1He_lYsMphHl41rpQSEUfTeYIj976Oz4",
	authDomain: "quadlink-c80dc.firebaseapp.com",
	databaseURL: folder,
	storageBucket: "quadlink-c80dc.appspot.com",
	};


	firebase.initializeApp(config);

	// const preObject = document.getElementById('object');

	const dbRefObject = firebase.database().ref().child(quad);

	dbRefObject.on('value', function(snapshot) {
		console.log(snapshot.val());
		up(po,snapshot.val());
	});

	const x_value = firebase.database().ref().child(quad).child("x_axis")

	x_value.on('value', function(snapshot) {
		console.log(snapshot.val())
		insidefun(inside, snapshot.val())
	});


	const y_value = firebase.database().ref().child(quad).child("y_axis")

	const z_value = firebase.database().ref().child(quad).child("y_axis")

	var LinkedObj = new links(x_value, y_value, z_value)
	console.log(LinkedObj.x_valuex)

	return LinkedObj;

	}