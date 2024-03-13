#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      this.object = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width === undefined || this.height === undefined) {
      console.log('');
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    if (this.width !== undefined && this.height !== undefined) {
      const exchanger = this.width;
      this.width = this.height;
      this.height = exchanger;
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
