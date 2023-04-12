#!/usr/bin/node
// script to print two arguments passed to it, in the following format: "is"
// Must use console.log(...) to print all output
// Not allowed to use var

const args = process.argv;
console.log(args[2] + ' is ' + args[3]);
