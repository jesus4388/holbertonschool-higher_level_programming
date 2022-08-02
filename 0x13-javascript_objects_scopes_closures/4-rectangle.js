#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      } 
    } else {
      for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
      }
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
