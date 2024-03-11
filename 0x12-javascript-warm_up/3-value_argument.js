#!usr/bin/node
const { argv } = require('process');
let count = 0;
argv.forEach(() => {
  count++;
});
if (count <= 2) {
  console.log('No argument');
} else {
  argv.forEach((val, index) => {
    console.log(`${index}: ${val}`);
  });
}
