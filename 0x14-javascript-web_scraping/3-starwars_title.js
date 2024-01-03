#!/usr/bin/node
// makes aget request to the starwars API

const request = require('request');
const ID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + ID;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('ERRO!', response.statusCode);
  }
});
