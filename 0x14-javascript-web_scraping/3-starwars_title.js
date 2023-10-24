#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, { json: true }, (err, res, body) => {
  if (err) console.log(err);
  console.log(body.title);
});
