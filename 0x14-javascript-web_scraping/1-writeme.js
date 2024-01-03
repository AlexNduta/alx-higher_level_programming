#!/usr/bin/node
// writes contents to a file
const fs = require('fs');
const arg1 = process.argv[2];
const arg2 = process.argv[3];

fs.writeFile(arg1, arg2, (err) => {
  if (err) {
    console.log(err);
  }
});
