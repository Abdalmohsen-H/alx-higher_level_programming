#!/usr/bin/node
// task 101 advanced
const dict = require('./101-data.js').dict;
// console.log(dict);
const newdict = {};
// for (const [key, value] of Object.entries(dict)){
//  console.log(`Key: ${key}, Value: ${value}`);
// }
for (const [key, value] of Object.entries(dict)) {
  if (newdict[value] === undefined) {
    // if this value doesn't exist, create it and assign empty array for now
    newdict[value] = []; // create empty array for this value
  }
  newdict[value].push(key);// push value to the array
}
console.log(newdict);
