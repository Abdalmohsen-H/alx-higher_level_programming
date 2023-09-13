#!/usr/bin/node
// converter
exports.converter = function (base) {
  return numb => numb.toString(base);
};
