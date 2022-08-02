#!/usr/bin/node
module.exports = class Rectangle {
  constructori (h, w) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }
};
