#!/usr/bin/node

const _argv = parseInt(process.argv[2]);
if (!isNaN(_argv)) {
  console.log('My number: ' + _argv);
} else {
  console.log('Not a number');
}
