#!/usr/bin/node

if (!process.argv[1]) {
  process.argv[1] = 'undefined';
} if (!process.argv[2]) {
  process.argv[2] = 'undefined';
}
console.log(process.argv[1], 'is', process.argv[2]);
