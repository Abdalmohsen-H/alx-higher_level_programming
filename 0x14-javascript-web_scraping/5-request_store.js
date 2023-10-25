#!/usr/bin/node
// import fs module (file system module)
const fs = require('fs');
const request = require('request');
// assign first argument to url
const url = process.argv[2];
// this could be done on different ways, ref: https://nodejs.dev/en/learn/reading-files-with-nodejs/
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  try {
    fs.writeFileSync(filePath, body, 'utf8');
  // console.log("file written successfully");
  } catch (err) {
    console.log(err);
  }
});
