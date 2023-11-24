function factorial (argv) {
  let fact = 1;

  for (let i = 0; i < argv; i++) {
    fact *= (argv - i);
  }

  return fact;
}
const result = factorial(5);
console.log(result);
