#!/usr/bin/node
//makes a GET request then prints users with completed tasks

const request = require('request');
const url = process.argv[2];

request(url, function(error, response, body){
    if (error){
        console.log(error)
    } else if (response.statusCode === 200) {
       body = JSON.parse(body);
       const output= body.results;
       for(let i in output){
           if (["comlepted"].value === true){
               console.log(["id"])
           }
       }
    } else {
        console.log(response.statusCode)
    }
});
