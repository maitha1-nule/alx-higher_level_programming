#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const sortedArgs = args.map(Number).sort((a, b) => a - b);
  const secondBiggest = sortedArgs[sortedArgs.length - 2];
  console.log(secondBiggest);
}
