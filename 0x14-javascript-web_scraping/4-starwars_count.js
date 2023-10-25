#!/usr/bin/node
// import fs module (file system module)
const request = require('request');
// assign first argument to url
const url = process.argv[2];
const searchPherase = 'api/people/18';

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  const count = (response.body.split(searchPherase).length) - 1;
  console.log(count);
});
