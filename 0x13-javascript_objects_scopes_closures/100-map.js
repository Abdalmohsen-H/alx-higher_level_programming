#!/usr/bin/node
// advanced task on map method on arrays
const impoDataMod = require('./100-data.js');
const impoList = impoDataMod.list;
console.log(impoList);
// (x, index) are args , while code after => is return on each array element
const mapList = impoList.map((item, index) => item * index);
console.log(mapList);
