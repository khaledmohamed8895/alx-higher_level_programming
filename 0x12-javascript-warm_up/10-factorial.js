#!/usr/bin/node
function fact (a) {
  if (!a) {
    return (1);
  } else {
    return a * fact(a - 1);
  }
}
console.log(fact(process.argv[2]));
