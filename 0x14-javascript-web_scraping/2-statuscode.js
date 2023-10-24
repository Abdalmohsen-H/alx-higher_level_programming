#!/usr/bin/node
// import fs module (file system module)
const request = require('request');
// assign first argument to url
const url = process.argv[2];
try {
  request.get(url, (err, response) => {
    console.log(response.statusCode);
  });
} catch (err) {
  console.log(err);
}
