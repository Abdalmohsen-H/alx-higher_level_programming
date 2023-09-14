#!/usr/bin/node
// calculate factorial of input number using recursion
// if input num is 1 or not a number then return 1
const inptNum = parseInt(process.argv[2]);
function Factorial (num) {
  if ((Number.isNaN(num)) || (num === 1)) {
    return 1;
  }
  return Factorial(num - 1) * num;
}
console.log(Factorial(inptNum));
