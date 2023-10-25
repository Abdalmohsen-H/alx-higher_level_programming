#!/usr/bin/node
// import request module
const request = require('request');
// import util module
const util = require('util');
// assign first argument to mvId
const mvId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + mvId;
const promisifedrequest = util.promisify(request);

async function getAlllNames (url) {
  try {
    const chrs = (await promisifedrequest(url, { json: true })).body.characters;
    for (const charUrl of chrs) {
      // console.log(charUrl);
      const resp = await promisifedrequest(charUrl, { json: true });

      const charName = resp.body.name;
      console.log(charName);
    }
  } catch (err) {
    console.log(err);
  }
}

getAlllNames(url);
