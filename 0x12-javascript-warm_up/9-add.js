#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const suma = parseInt(a) + parseInt(b);
    console.log(suma);
  }
}
add(process.argv[2], process.argv[3]);
