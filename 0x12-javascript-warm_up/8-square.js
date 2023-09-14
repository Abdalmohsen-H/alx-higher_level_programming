#!/usr/bin/node
// task 8 print square
const sizeArg = process.argv[2];
if (sizeArg === undefined) {
  console.log('Missing size');
} else {
  const size = parseInt(sizeArg, 10);
  if (isNaN(size)) {
    console.log('Missing size');
  } else {
    for (let vunit = 0; vunit < size; vunit++) {
      console.log('X'.repeat(size));
    }
  }
}
