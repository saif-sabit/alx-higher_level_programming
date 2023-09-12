#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let i = 0; process.argv[2] > i; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
