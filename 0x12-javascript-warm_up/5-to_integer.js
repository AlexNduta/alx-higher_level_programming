#!/usr/bin/node

const argv = Math.floor(Number(process.argv[2])); // convert the argument to an integer
const text = 'My number: ';
if (isNaN(argv)) {
  console.log('Not a number');
} else if (argv !== undefined) {
  console.log(text, argv);
}
