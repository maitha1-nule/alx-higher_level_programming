#!/usr/bin/node
const arg = process.argv[2];
const num = Number(arg);
if (!Number.isInteger(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
