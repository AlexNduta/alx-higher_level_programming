#!/usr/bin/node
const varg = process.argv;

for (let i = 2; i <= varg.length - 1; i++) {
  if (varg[i] !== null) {
    console.log(varg[i]);
  } else {
    console.log('No argument');
  }
}
