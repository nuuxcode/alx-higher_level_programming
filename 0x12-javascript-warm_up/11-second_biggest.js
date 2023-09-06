#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) console.log(0);
else {
  console.log(argv.slice(2).sort((a, b) => b - a)[1]);
}
