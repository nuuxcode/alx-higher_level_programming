#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];
try {
  fs.writeFileSync(file, string, { encoding: 'utf8' });
} catch (err) {
  console.error(err);
}
