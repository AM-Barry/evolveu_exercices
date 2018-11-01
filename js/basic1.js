console.log("Hello world from Barry");
function myfunction(){
	console.log("I'm a console.log");
	alert("I'm an alert in myfunction");
}
var count = 0;
function myfunctionmouse() {
	console.log("You are a mouse over");
	count +=1;
	document.getElementById("mydiv").innerHTML += "<br>You are mouse over "+count; 

}

function addtext(){
	document.getElementById("mydiv").innerHTML += "<br>added text example" ;
}

function move(){
	var x = document.getElementById("cx").value ;
    var y = document.getElementById("cy").value ;
	document.getElementById('circ1').setAttribute("cx", x);
	document.getElementById('circ1').setAttribute("cy", y);
	// document.getElementById('rect1').setAttribute("x", y);

}

 function myFunction() {
    var y = document.getElementById("txt1").value;
    var z = document.getElementById("txt2").value;
    var x = +y + +z;
    document.getElementById("demo").innerHTML = x;
 }