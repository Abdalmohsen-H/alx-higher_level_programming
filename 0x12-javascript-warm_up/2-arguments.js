#!/usr/bin/node
/* task 2
* A. Hesham
 */

const myArgs = process.argv.length;
if (myArgs === 2) {
  console.log('No argument');
} else if (myArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
