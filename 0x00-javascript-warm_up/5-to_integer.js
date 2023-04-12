#!/usr/bin/node
// A script to print "My number: <first argument converted in integer>"
// if first argument can be converted to integer
// If argument can’t be converted to integer, print “Not a number”
// You must use console.log(...) to print all output
// You are not allowed to use var
// You are not allowed to use try/catch
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[2]));
}
