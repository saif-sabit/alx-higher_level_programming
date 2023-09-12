#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        if (c) {
          s += c;
        } else {
          s += 'X';
        }
      }
      console.log(s);
    }
  }
}
module.exports = Square;
