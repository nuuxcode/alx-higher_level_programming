#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
try {
  const data = fs.readFileSync(file, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
