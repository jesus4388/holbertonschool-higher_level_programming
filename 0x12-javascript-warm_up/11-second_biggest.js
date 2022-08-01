#!/usr/bin/node
if (process.argv.length > 3) {
  const array = [];
  for (let i = 2, j = 0; i < process.argv.length; i++, j++) {
    array[j] = process.argv[i];
  }
  array.sort();
  let a = 0;
  let b = 0;
  for (let c = 0; c < array.length; c++) {
    if (a < array[c]) {
      b = a;
      a = array[c];
    }
  }
  console.log(b);
} else {
  console.log(1);
}
