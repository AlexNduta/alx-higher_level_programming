#!/usr/bin/node

const argv = process.argv[2];
const text = 'My number: ';
if (isNaN(argv)) {
  console.log('Not a number');
} else if (argv !== undefined) {
  console.log(text, argv);
}
