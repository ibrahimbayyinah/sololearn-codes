const greet = x => {return `Hello there, ${x}.`;} // return must be there, otherwise function will return 'undefined'

let name = prompt("What is your name?");
alert(greet(name));
