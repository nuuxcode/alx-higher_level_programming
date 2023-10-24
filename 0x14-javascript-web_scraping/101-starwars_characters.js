#!/usr/bin/node
const request = require('request');
const util = require('util');
const id = process.argv[2];

const prequest = util.promisify(request);

(async () => {
  try {
    const body = (await prequest(`https://swapi-api.alx-tools.com/api/films/${id}`, { json: true })).body;
    for (const url of body.characters) {
      const body = (await prequest(url, { json: true })).body;
      console.log(body.name);
    }
  } catch (err) {
    console.log(err);
  }
})();
