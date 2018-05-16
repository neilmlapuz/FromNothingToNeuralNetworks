//flag to check to see if something is drawn on the canvas
var drawn = false;
(function()
{
	
	var drawing = false;
	//Gets the canvas tag
	var canvas = document.getElementById("canv");
	var context = canvas.getContext("2d");

	//Canvas features
	canvas.width = 280;
	canvas.height = 280;
	context.fillStyle="white";
	context.fillRect(0,0,canvas.width,canvas.height);
	context.color = "black";
	context.lineWidth = 10;
    context.lineJoin = context.lineCap = 'round';
	
	clear();

	canvas.addEventListener("mousemove", function(event){
		var mousePosition = getMousePos(canvas,event);
		var posX = mousePosition.x;
		var posY = mousePosition.y;
		draw(canvas,posX,posY);
	}, false);

	//Set drawing variable true to draw
	canvas.addEventListener("mousedown", function(){
		drawn = true;
		drawing = true;
	});

	//User stops its click -- draw stops
	canvas.addEventListener("mouseup", function(){
		drawing = false;
	}, false);

	function draw(canvas,posX,posY){
		var ctx = canvas.getContext("2d");
		if(drawing){
			canvas.style.cursor="crosshair";
			ctx.lineWidth = 15;
			ctx.lineJoin = "round";
			ctx.lineCap = "round";
		
			ctx.beginPath();
			ctx.moveTo( posX, posY );
			ctx.lineTo( posX, posY );
			ctx.closePath();
			ctx.stroke();
		}
	};

	//This returns the position of the mouse when move in the canvas 
	function getMousePos(canvas,event){
		var rect = canvas.getBoundingClientRect();
		//returns the values of the coordinates of the mouse
		return{
			x:event.clientX - rect.left, //subtract to get the position of the mouse related to the canvas
			y:event.clientY - rect.top
		};
	};

	function clear()
	{
		//function to reset the canvas when the reset button is clicked
		var clearButton = document.getElementById("clear").addEventListener("click",function()
		{
			$("#predictionResult").text("RESULT");
			drawn = false;
			context.clearRect(0,0,280,280);
			context.fillRect(0,0,canvas.width,canvas.height);
			
		});
	}
}());