#!/usr/bin/node
// import fs module (file system module)
const request = require('request');
// assign first argument to url
const url = process.argv[2];
request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  console.log('code:', response.statusCode);
});
