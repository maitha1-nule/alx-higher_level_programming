#!/usr/bin/node
const Rectangle = require('./5-square.js');
class Square extends Rectangle {
charPrint(c) {
if ( c === undefined ) {
c = 'X';
}
for (let i = 0; i < this.height; i++) {
if (i < this.width) {
console.log(c.repeat(this.width));
} else {
console.log(c.repeat(this.width));
}
}
}
}
module.exports = Square;
