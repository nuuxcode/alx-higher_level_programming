#!/usr/bin/node
const { argv } = require('process');
const Str = 'C is fun';
let x = parseInt(argv[2], 10);
if (!isNaN(x)) {
  while (x > 0) {
    console.log(Str);
    x--;
  }
} else console.log('Missing number of occurrences');
