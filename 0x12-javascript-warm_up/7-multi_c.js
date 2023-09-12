#!/usr/bin/node
/*
* print a specified string as much as user requires
* user will enter required number of printing as argument
* handle cases when no argument or argument isn't a number
*/
let args = process.argv
if (args[2] === 'undefined'){
    console.log('Missing number of occurrences');
}
let num = parseInt(args[2], 10);
if (isNaN(num)){
    console.log('Missing number of occurrences');
}
for (let count = 0; count < num; count++){
    console.log('C is fun');
}
