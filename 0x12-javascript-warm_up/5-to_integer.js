#!/usr/bin/node
const { argv } = require('process');
const myNumber = 'My number: ';
if (!isNaN(parseInt(argv[2], 10))) console.log(myNumber + parseInt(argv[2], 10));
else console.log('Not a number');
