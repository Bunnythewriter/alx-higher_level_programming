#!/usr/bin/node

let myArgCount = process.argv.length -2;

if (myArgCount > 0){
    if (myArgCount > 1){
        console.log("Arguments found");
    } else if (myArgCount === 1){
        console.log("Argument found");
    } 
} else {
    console.log("No arguments found")
}
