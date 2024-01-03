#!/usr/bin/node 
//makes aget request to the starwars API

const request = require('request');
const ID = process.argv[2];
const url = "https://swapi-api.alx-tools.com/api/films/:id"
request(url, function(error, response, body)){
    console.log(body);
});
