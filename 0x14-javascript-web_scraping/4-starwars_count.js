#!/usr/bin/node
// import fs module (file system module)
const request = require('request');
// assign first argument to baseUrl
const baseUrl = process.argv[2];
const charcId = 18
const filter = 'people'
const url = baseUrl + '?' + filter + '=' + charcId

request.get(url, (error, response) => {
	if (error) {
		console.log(error);
	}
	console.log(JSON.parse(response.body).count);
});
