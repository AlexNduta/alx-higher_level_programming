#!/usr/bin/node

const argv = parseInt(process.argv[2], 10); // convert the argument to an integer
const text = 'My number: ';
// check if the argument is a number
if (isNaN(argv)) {
  console.log('Not a number');
} else {
  console.log(text, argv);
}