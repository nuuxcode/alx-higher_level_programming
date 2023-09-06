#!/usr/bin/node
const { argv } = require('process');
const a = parseInt(argv[2], 10);
const b = parseInt(argv[3], 10);
function add (a, b) {
  return a + b;
}
console.log(add(a, b));
