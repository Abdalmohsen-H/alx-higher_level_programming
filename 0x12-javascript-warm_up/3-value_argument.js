#!/usr/bin/node
/* task 3
* A. Hesham
* just another task that prints first argument passed to it
* first argument will always be in process.argv[2] if exists
* as process.argv[0], [1] already have default values
* as argv[0] is process.execPath
* and argv[1] is the path to the JavaScript file being executed
*/

const myArgs = process.argv[2];
if (typeof myArgs === 'undefined') {
  console.log('No argument');
} else {
  console.log(myArgs);
}
