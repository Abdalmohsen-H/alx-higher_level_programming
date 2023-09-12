#!/usr/bin/node
/* task 2
* A. Hesham
* exercise on reading argument using process.argv
* reference : https://nodejs.org/docs/latest/api/process.html#processargv
*/

const myArgs = process.argv.length;
if (myArgs === 2) {
  console.log('No argument');
} else if (myArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
