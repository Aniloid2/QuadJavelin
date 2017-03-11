var Setcanvas = function () {
	var scene = new THREE.Scene();
	scene.background = new THREE.Color( 0xffffff );
	var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 1, 10000);
	var renderer = new THREE.WebGLRenderer();
	renderer.setSize(window.innerWidth, window.innerHeight);
	document.body.appendChild(renderer.domElement);





	var pyramidgeometry = new THREE.CylinderGeometry(0, 300, 800, 4,20, false);
	var pyramidmaterial = new THREE.MeshBasicMaterial({wireframe: true, color: 0x0000ff});
	var pyramid = new THREE.Mesh(pyramidgeometry, pyramidmaterial);
	pyramid.position.set(0.0,0,0);
	scene.add(pyramid);






	camera.position.z = 1000;        
	function render() {
	requestAnimationFrame(render);
	// pyramid.rotation.x += 0.01; //roll
	// // // cube.rotation.y += 0.01; //yaw
	// pyramid.rotation.z += 0.02; //pitch
	rotate();

	var rotate = function() {
		pyramid.rotation.x += 0.01; //roll
	// // cube.rotation.y += 0.01; //yaw
		pyramid.rotation.z += 0.02; //pitch

	}


	renderer.render(scene, camera);
	};
	render();
}