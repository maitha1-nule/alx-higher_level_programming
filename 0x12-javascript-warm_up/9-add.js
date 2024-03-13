#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
const args = process.argv.slice(2);
if (args.length !== 2) {
  console.log('NaN');
} else {
  console.log(add(args[0], args[1]));
}
