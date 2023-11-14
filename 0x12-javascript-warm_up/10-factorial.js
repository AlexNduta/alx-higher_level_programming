#!/usr/bin/node
// formulae: n!= n*n(n-1))
const size = parseInt(process.argv[2], 10);

function factorial (n) {
  if (isNaN(size)) {
    return 1;
  } else if (n === 0) {
    return (1);
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(size));
