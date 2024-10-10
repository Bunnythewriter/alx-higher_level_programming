#!/usr/bin/node

let args = process.argv[2]

if (args){
    console.log(args);
} else{
    console.log("No argument.");
}