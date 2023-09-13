#!/usr/bin/node
// Array.prototype.filter() takes an array, decides
// element by element if it should keep it or not and
// returns an array with the kept elements only
// const numbers = [0, 1, 2, 3, 4, 5, 6];
// const evenNumbers = numbers.filter(n => n % 2 === 0); // [0, 2, 4, 6]
exports.nbOccurences = function (list, searchElement) {
  return list.filter(item => item === searchElement).length;
};
