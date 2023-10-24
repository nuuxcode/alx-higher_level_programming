#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res) => {
  if (err) console.log(err);
  console.log('code:', res.statusCode);
});
