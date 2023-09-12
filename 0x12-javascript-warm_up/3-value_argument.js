#!/usr/bin/node
/* task 3
* A. Hesham
* just another task
 */

const myArgs = process.argv[2];
if (typeof myArgs === 'undefined') {
  console.log('No argument');
} else {
  console.log(myArgs);
}
