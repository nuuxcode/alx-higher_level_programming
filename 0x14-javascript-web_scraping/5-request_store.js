#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, (err, res, body) => {
  if (err) console.log(err);
  try {
    fs.writeFileSync(file, body, { encoding: 'utf8' });
  } catch (err) {
    console.error(err);
  }
});
