/*************************
* Variables and data types

var firstName = 'John';
console.log(firstName);

var lastName = 'Smith';
var age = 28;

var fullAge = true;
console.log(fullAge);

//variable naming rules
var job;
console.log(job);
job = 'Teacher';
console.log(job);

/*************************
* Variables and data types

// Type coercion
var firstName= 'John';
var age = 28;
console.log(firstName +' '+ age);

var job, isMarried;
job = 'teacher';
isMarried = false;
console.log(firstName + ' is a ' + age + ' year old ' + job + '.Is he married? ' + isMarried);

// Variable mutation
age = 'twenty eight';
job = 'driver';

alert(firstName + ' is a ' + age + ' year old ' + job + '.Is he married? ' + isMarried);

var lastName = prompt('what is his last Name?');
console.log(firstName + ' ' + lastName);
*/

/*************************
* Basic operators

var year, yearJohn, yearMark;
now = 2018;
ageJohn = 28;
ageMark  = 33;

// Math operators
yearJohn = now - ageJohn;
yearMark = now - ageMark;

console.log(yearJohn);
console.log(now + 2);
console.log(now * 2);
console.log(now / 10);

// Logical operators
var johnOlder = ageJohn < ageMark;
console.log(johnOlder);

// typeof operator
console.log(typeof johnOlder);
console.log(typeof ageJohn);
console.log(typeof 'Mark is older than John');
var x;
console.log(typeof x);

var markHeight = 2;
var johnHeight = 1;
var markMass = 50;
var johnMass= 60;

var markBmi, johnBmi;

markBmi = markMass / markHeight * markHeight;
johnBmi = johnMass / johnHeight * johnHeight;

var ismarkBmi = markBmi < johnBmi;
console.log("Mark's BMI is: "+ markBmi);
console.log("John''s BMI is: "+ johnBmi);
console.log( 'Is Mark BMI higher that John BMI: ' + ismarkBmi);
*/
/*************************
* the ternary operator and switch statement

var firsName = 'John';
var age = 17;

//Ternary operartor
age >= 18 ? console.log(firsName + ' drinks beer.'): console.log(firsName + ' drinks juice.');

var drink = age >= 18 ? 'beer' : 'juice';
console.log(drink);

// Switch statement
var job = 'driver';
switch(job) {
    case 'teacher':
        console.log(firsName + ' teaches kids how to code.');
        break;
    case 'driver':
        console.log(firsName + ' drives kids to school.');
        break;
    case 'designer':
        console.log(firsName + ' designs websites.');
        break;
    default:
        console.log(firsName + ' does somethon else.');
}
*/
// Coding challenge 2

/*switch(true) {
    case johnAve > markAve :
            console.log('John\'s team wins with average score: ' + johnAve);
        break;
    case johnAve < markAve :
            console.log('Mark\'s team wins with average score:' + markAve);   break;  
    case johnAve == markAve :
            console.log('same average score:' + johnAve +'==' + markAve);
                
}
*/
var maryScore1 = 110;
var maryScore2 = 120;
var maryScore3 = 103;
var johnScore1 = 110;
var johnScore2 = 120;
var johnScore3 = 103;
var markScore1 = 109;
var markScore2 = 120;
var markScore3 = 103;
johnAve = (johnScore1+johnScore2+johnScore3)/3;
markAve = (markScore1+markScore2+markScore3)/3;
maryAve = (maryScore1+maryScore2+maryScore3)/3;

switch(true){
        case (johnAve > markAve && johnAve> maryAve):
            console.log('John\'s team wins with average score: ' + johnAve);
        break;
        case (markAve > johnAve && markAve> maryAve):
            console.log('Mark\'s team wins with average score: ' + markAve);
        break;
        case (maryAve > johnAve && maryAve> markAve):
            console.log('Mary\'s team wins with average score: ' + maryAve);
        break;
        default:
        console.log('There is a draw');
            
}






