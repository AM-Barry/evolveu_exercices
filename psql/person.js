class Person {
    constructor (name, age, bankAmount) {
        this.name = name;
        this.age = age;
        this.bankAmount = bankAmount;
    }
    birthday() {
        this.age += 1;
    }
    
}

class Farmer extends Person {
    constructor(name, age,bankAmount, pay) {
        super(name, age, bankAmount);
        this.pay = pay;  
        this.counter = 0;
    }
    payment(pay) {
        
        this.counter ++;
        if (this.counter == 12) {
            this.bankAmount += this.pay;
            this.counter = 0;
        }
        
    }
        
    
}


class Fsd extends Person {
    constructor(name, age, bankAmount, pay) {
        super(name, age, bankAmount);
        this.pay = pay;
    }
    payment() {
        this.bankAmount += this.pay;
    }
}


class Clerk extends Person {
    constructor(name, age, bankAmount, rate, hours) {
        super(name, age, bankAmount);
        this.rate = rate;
        this.hours = hours;
    
    }
    payment() {
        this.bankAmount += this.rate * this.hours;
        
    }
}

var Ryker = new Fsd('Ryker', 33, 0, 15000);

var Jane = new Clerk ('Jane', 50, 0, 15, 150);

var Barry = new Farmer ('Barry', 30, 0, 100000);

var Mike = new Fsd ('Mike', 25, 0, 5000);

//var personArray = [Ryker, Jane, Barry, Mike];
//console.log(personArray);
//
var employees = [];

employees.push(Ryker,Jane, Barry, Mike);

//console.log(employees);

for (var i=0; i<employees.length; i++) {
    employees[i].payment();
    console.log(employees[i]);
}






 
