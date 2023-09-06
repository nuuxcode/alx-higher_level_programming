#!/usr/bin/node
const { argv } = require('process');
const firstArgv = argv[2];
const secondArgv = argv[3];
const middleString = ' is ';
console.log(firstArgv + middleString + secondArgv);
