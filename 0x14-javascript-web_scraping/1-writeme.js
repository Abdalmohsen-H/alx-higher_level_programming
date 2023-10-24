#!/usr/bin/node
// import fs module (file system module)
const fs = require('fs');
// assign first argument to file_path
const filePath = process.argv[2];
// this could be done on different ways, ref: https://nodejs.dev/en/learn/reading-files-with-nodejs/
const content = process.argv[3];
try {
  fs.writeFileSync(filePath, content, 'utf8');
  // console.log("file written successfully");
} catch (err) {
  console.log(err);
}
