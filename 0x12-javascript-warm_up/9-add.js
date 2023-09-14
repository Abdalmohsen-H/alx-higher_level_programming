#!/usr/bin/node
// task 9 function to add 2 inputs
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const num1 = parseInt(arg1, 10);
const num2 = parseInt(arg2, 10);

function add (a, b) {
  return (a + b);
}
console.log(add(num1, num2));
