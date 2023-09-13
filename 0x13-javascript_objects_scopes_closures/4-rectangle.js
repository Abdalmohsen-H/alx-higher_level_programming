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

  rotate () {
    // exchanges the width and the height of the rectangle
    const tempWidth = this.width;
    this.width = this.height;
    this.height = tempWidth;
    // or just use the following
    // [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
