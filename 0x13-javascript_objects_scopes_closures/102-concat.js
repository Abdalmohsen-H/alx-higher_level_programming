#!/usr/bin/node
// task 102 read content from 2 given files paths
// then concatnate those contents and write them to third given file path
const fs = require('fs');
// read first 2 argument file pathes and get content
const file1 = fs.readFileSync(process.argv[2]);
const file2 = fs.readFileSync(process.argv[3]);
// concatnate then write
fs.writeFileSync(process.argv[4], file1 + file2, 'utf-8');
