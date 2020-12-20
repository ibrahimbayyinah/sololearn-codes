/*
There is something interesting happening when I don't use the parseFloat function:
when I input the values for a and b as 90 and 1 respectively, the message "your numbers combined 
are bigger than 100" gets printed to the console. It should normally print "smaller than 100".

Does anyone know why this happens?
*/


// let a = parseFloat(prompt("enter a number"));
// let b = parseFloat(prompt("enter another number"));

let a = prompt("enter a number");
let b = prompt("enter another number");

// document.write(`Value of a: ${a}. Value of b: ${b}.`);
console.log(`Value of a: ${a}. Value of b: ${b}.`);

let msg = `Hmm great choice. Your numbers combined are ${(a+b > 100) ? "bigger than 100.":"smaller than 100."}`;
console.log(msg);
