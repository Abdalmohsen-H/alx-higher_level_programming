#!/usr/bin/node
// task 101
exports.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
};
