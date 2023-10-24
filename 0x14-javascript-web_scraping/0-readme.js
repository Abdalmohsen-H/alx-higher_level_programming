#!/usr/bin/node
// import fs module (file system module)
const fs = require('fs');
// assign first argument to file_path
const file_path = process.argv[2];
// this could be done on different ways, ref: https://nodejs.dev/en/learn/reading-files-with-nodejs/
try{
	const rdata = fs.readFileSync(file_path, 'utf8');
	console.log(rdata);
} catch(err) {
	console.log(err);
};

