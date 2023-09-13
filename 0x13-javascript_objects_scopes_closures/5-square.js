#!/usr/bin/node
/*
 * inheritance in javascipt oop using extends
 * also we will import the parent class using require(filepath)
*/
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    // pass square size as square width and hight to the
    // inherited rectangle constructor method
    super(size, size);
  }
};
