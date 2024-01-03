#!/usr/bin/node
// read and prints cntents of a file
const fs = require('fs'); // import 'fs' mosule for reading files
const input = process.argv[2]; // create the input variable

// read the file using the `readFile` function
fs.readFile(input, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
