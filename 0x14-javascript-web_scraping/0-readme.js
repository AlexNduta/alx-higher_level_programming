#!/usr/bin/node
//read and prints cntents of a file
const fs = require('fs'); //import 'fs' mosule for reading files
const input = process.argv[2];  //create the input variable

//read the file using the `readFile` function
fs.readFile(input, function(err,data)=> {
    if (error) {
        console.error("Error" + error);
    } else {
    console.log(data.toString());
    }
});
