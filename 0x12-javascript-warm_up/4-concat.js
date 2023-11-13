#!/usr/bin/node

if (!process.argv[2]) {
  process.argv[2] = 'undefined';
} if (!process.argv[3]) {
  process.argv[2] = 'undefined';
}
console.log(process.argv[2], 'is', process.argv[3]);
