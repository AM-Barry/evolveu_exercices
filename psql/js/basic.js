/*
var myPrint = function() {
    console.log(myPrint);    
}


var myModule = (function() {
    var myString = 'My value';
    console.log('Hello World');
    
    
    function myFunc() {
        console.log("I am in myFunc");
    }
    
    return {
        stuff : 'some stuff',
        myNum : 42,
        yourString : myString,
        yourFunc : myFunc
    };
})();

console.log(myModule);
console.log(myModule.myString);
myModule.yourFunc();
myModule.myPrint;
*/

function moveText(){
    var x = document.getElementById("textarea").value;
    document.getElementById("movebottom").innerHTML+= x +'</br>';
    document.getElementById('textarea').value='';
    
};

 var playModule = function() {
     document.getElementById("json").onclick = screenPrint;
     document.getElementById("myArray").onclick = myArray;
     document.getElementById("myObject").onclick = myObject;
     document.getElementById("mydivBuilder").onclick = addDiv;
     //document.getElementById("main").onclick = removeDiv;
     
     //document.getElementById("json").onclick = convertString;
     
     //var myArray = [1, 7, 23, 24];
     var myObject = {'AB' : 'ALberta',
                     'ON' : 'Ontario',
                     'BC' : 'British C'};
     var obj;
     var counter = 0;
     function convertString() {
         jsonString =  document.getElementById("textarea");
         obj = JSON.parse(jsonString.value);
         //console.log(obj);
         document.getElementById("listjson").innerHTML = obj;
     };
     
     function myArray() {
         //arr1 = obj;
         for (i = 0; i <obj.length; i++) {
           //document.getElementById("listarray").innerHTML+=(myArray[i])+'</br>';
             console.log(obj[i]);
         }
     };
     
     function myObject() {
         
         for (i in myObject) {
             //document.getElementById("listobject").innerHTML+=(myObject[i])+'</br>';
             console.log(i, myObject[i]);
         }
     };
         
     function screenPrint() {
         console.log("I am JSON in playModule");
         convertString();
         myArray();
         var maxArray = Math.max.apply(Math, obj);
         var minArray = Math.min.apply(Math, obj);
         document.getElementById("listarray").innerHTML = minArray;
         document.getElementById("listobject").innerHTML = maxArray;
     }
    
     return {
         
     }
     
     
     function addDiv() {   
        var div = document.createElement("div");
        div.style.width = "150px";
        div.style.height = "150px";
        //div.style.background = "red";
        div.style.float = "left";
        div.style.border = "1px solid black";
        div.style.textAlign = "center";
        div.style.marginTop = "10px";
        div.style.marginRight = "2px";
        //div.style.color = "white";
        div.onclick = doSomething;
        div.innerHTML = counter;
        document.getElementById("main").appendChild(div);
        counter++;
        
        
     }
     
     
     function doSomething(e) {
            e.target.remove(); 
              
        }
     
     
     
}();
