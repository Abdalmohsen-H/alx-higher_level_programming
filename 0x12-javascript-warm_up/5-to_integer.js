#!/usr/bin/node
/* task 5
* A. Hesham
* just another task
 */

const myArg = process.myArgv[2];
const num = parseInt(myArg, 10);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
