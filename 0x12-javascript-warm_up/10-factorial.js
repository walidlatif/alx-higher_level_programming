const { argv } = require('node:process');

let fact = 1;

for (let i = 0; i < argv[2]; i++) {
  fact *= (argv[2] - i);
}
console.log(fact);
