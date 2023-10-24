#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) console.log(err);
  const results = {};
  for (const i in body) {
    if (results[body[i].userId] === undefined) {
      results[body[i].userId] = 0;
    }
    if (body[i].completed === true) {
      results[body[i].userId] += 1;
    }
  }
  console.log(results);
});
