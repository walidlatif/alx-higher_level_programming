#!/usr/bin/node

const _argv = parseInt(process.argv[2]);
if (isNaN(_argv)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < _argv; i++) {
    console.log('X'.repeat(_argv));
  }
}
