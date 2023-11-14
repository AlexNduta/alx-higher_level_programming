#!/usr/bin/node
const secondArg = process.argv[2];

if (secondArg === undefined) {
  console.log('No argument');
} else {
  console.log(secondArg);
}
