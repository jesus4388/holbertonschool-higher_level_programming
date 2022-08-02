#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }

  rotate () {
    const swap = this.height;
    this.height = this.width;
    this.width = swap;
  }
};
