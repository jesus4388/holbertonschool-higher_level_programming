#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    array[j] = list[i];
  }
  return array;
};
