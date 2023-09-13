#!/usr/bin/node
// count argument and return them

let counter = 0;
exports.logMe = function (item) {
  console.log(`${counter++}: ${item}`);
};
