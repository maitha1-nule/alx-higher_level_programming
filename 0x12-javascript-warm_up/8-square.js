#!/usr/bin/node
const arg = process.argv[2];
const square = Number(arg);
if (!Number.isInteger(square)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < square; i++) {
    let row = '';
    for (let j = 0; j < square; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
