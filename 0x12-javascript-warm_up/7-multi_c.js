#!/usr/bin/node
const str = 'C is fun';
const argv = parseInt(process.argv[2], 10);
if (argv === undefined || isNaN(argv)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < argv; i++) {
    console.log(str);
  }
}
