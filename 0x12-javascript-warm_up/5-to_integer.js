#!/usr/bin/node
/* task 5
* A. Hesham
* convert 1st arg into INT if it is a Number
 */

const myArg = process.argv[2];
const num = parseInt(myArg, 10);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
