

function callable(LinkObj) {

		console.log(LinkObj.y_valuey)

		var dps = []; // dataPoints

		var chart = new CanvasJS.Chart("chartContainer",{
			title :{
				text: "Live Random Data"
			},			
			data: [{
				type: "line",
				dataPoints: dps 
			}]
		});

		var xVal = 0;
		var yVal = 0;	
		var updateInterval = 100;
		var dataLength = 250; // number of dataPoints visible at any point

		var updateChart = function (count, y_value) {
			console.log(y_value)
			count = count || 1;
			// count is number of times loop runs to generate random dataPoints.
			console.log(count)

			if (y_value != undefined) {
				offset = y_value;
			}
			else {
				offset = 0;
			}
			for (var j = 0; j < count; j++) {	
				yVal = offset;
				dps.push({
					x: xVal,
					y: yVal
				});
				xVal++;
			};
			if (dps.length > dataLength)
			{
				dps.shift();				
			}
			
			chart.render();		

		};

		



		// generates first set of dataPoints
		updateChart(dataLength); 

		// update chart after specified time. 
		//setInterval(function(){updateChart()}, updateInterval); 

		LinkObj.x_acc.on('value', function(snapshot) {
		console.log(snapshot.val())
		updateChart( undefined , snapshot.val())
		});

	}

