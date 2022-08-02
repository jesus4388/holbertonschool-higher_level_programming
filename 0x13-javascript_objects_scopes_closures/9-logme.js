#!/usr/bin/node
let i = 0;
exports.logMe = function (item) {
  let line = i + ': ' + item;
  console.log(line);
  i++;
}
