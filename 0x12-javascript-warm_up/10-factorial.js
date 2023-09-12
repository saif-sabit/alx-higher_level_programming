#!/usr/bin/node
function facrtorial (a) {
  if (a === 0 || isNaN(a)) {
    return (1);
  }
  return a * facrtorial(a - 1);
}
console.log(facrtorial(parseInt(process.argv[2])));
