#!/usr/bin/node
const { argv } = require('process');
const a = parseInt(argv[2], 10);
function factorial (a) {
  if (a <= 1) return 1;
  return a * factorial(a - 1);
}
if (isNaN(a)) console.log(1);
else console.log(factorial(a));
// n * (n - 1) * (n-2) ... (1)
