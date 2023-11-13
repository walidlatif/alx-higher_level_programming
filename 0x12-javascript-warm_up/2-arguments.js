#!/usr/bin/node
const { argv } = require('process');
argv.length <= 2 ? console.log('No argument') : argv.length >= 3 ? console.log('Argument found') : console.log('Argument found');
