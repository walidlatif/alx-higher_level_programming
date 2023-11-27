#!/usr/bin/node

function computeFactorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num < 0) {
    return Infinity;
  } else if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * computeFactorial(num - 1);
  }
}

const args = process.argv.slice(2);
const input = parseInt(args[0]);

const factorial = computeFactorial(input);
console.log(factorial);
