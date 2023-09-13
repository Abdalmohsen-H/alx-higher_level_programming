#!/usr/bin/node
// task 1: create rectangle class with constructor
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let vunit = 0; vunit < this.height; vunit++) {
      console.log('X'.repeat(this.width));
    }
  }
};
