#!/usr/bin/node
// import fs module (file system module)
const request = require('request');
// assign first argument to mvId
const mvId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + mvId;

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(response.body).title);
});
