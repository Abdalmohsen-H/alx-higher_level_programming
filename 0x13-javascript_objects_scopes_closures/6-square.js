#!/usr/bin/node
/*
 * inheritance in javascipt oop using extends
 * also we will import the parent class using require(filepath)
*/
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    // draw square with user defined char , otherwise use default X
    if (c === undefined) {
      this.print();
    } else {
      for (let vunit = 0; vunit < this.height; vunit++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
