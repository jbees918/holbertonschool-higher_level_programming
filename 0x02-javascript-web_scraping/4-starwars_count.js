#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const title in data) {
      const charList = data[title].characters;
      for (const person in charList) {
        if (charList[person].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
