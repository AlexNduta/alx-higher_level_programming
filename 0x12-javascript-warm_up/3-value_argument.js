#!/usr/bin/node
const varg = process.argv;

if (varg.length <= 2) {
  console.log('No argument');
} else {
  console.log(varg[2]);
}
