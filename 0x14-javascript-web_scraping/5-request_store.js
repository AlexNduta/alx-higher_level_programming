#!/usr/bin/node
// makes GET request and saves output in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url).pipe(fs.createWriteStream(fileName));
