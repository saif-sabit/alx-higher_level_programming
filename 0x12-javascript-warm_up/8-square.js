#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let i = 0; process.argv[2] > i; i++) {
    let x = '';
    for (let j = 0; process.argv[2] > j; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
