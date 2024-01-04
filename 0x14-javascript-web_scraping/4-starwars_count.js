#!/usr/bin/node
// lists mnumber of fils where "Wedge Antilles” is present

const request = require('request');
const URL = process.argv[2];

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    const films = body.results;
    let count = 0;
    // loop through films then characters array and increament it everytime
    for (const i in films) {
      const chars = films[i].characters;
      for (const x in chars) {
        if (chars[x].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(response.statusCode);
  }
});
