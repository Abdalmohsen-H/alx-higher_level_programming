#!/usr/bin/node
// reverse array without using .reverse()
exports.esrever = function (list) {
  const reversedArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedArray.push(list[i]);
  }
  return reversedArray;
};
