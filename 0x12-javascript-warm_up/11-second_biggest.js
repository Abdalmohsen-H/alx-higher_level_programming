#!/usr/bin/node
// find second biggest integer in input list of arguments
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  // Converts the array of strings to an array of numbers then sort
  const sortedArgs = args.map(Number).sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
