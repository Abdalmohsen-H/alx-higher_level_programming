#!/usr/bin/node
// import request module
const request = require('request');
// assign first argument to url
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  const jsonResp = JSON.parse(response.body);
  const dictin = {};
  // or for (const todo in response) { };
  jsonResp.forEach(todo => {
    if (todo.completed) {
      dictin[todo.userId] = (dictin[todo.userId] || 0) + 1;
    }
  });
  console.log(dictin);
});
