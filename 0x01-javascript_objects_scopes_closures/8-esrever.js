#!/usr/bin/node
// Write a function that returns reversed version of a list:
// Prototype: exports.esrever = function (list)
// You are not allow to use built-in method reverse

exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
