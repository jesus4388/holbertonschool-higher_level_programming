#!/usr/bin/node
let i = 0;
exports.logMe = function (item) {
  const line = i + ': ' + item;
  console.log(line);
  i++;
};
