#!/usr/bin/node
// print the status code of the GET request
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  // console.error('error:'.error);
  console.log('code:', response && response.statusCode);
});
