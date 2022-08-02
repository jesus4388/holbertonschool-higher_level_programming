#!/usr/bin/node
exports.converter = function (base) {
  return function conver (num) {
    return num.toString(base);
  };
};
