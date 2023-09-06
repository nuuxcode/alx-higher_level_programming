#!/usr/bin/node
const { argv } = require('process');
const Str = 'X';
const x = parseInt(argv[2], 10);
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log(Str.repeat(x));
  }
} else console.log('Missing size');
