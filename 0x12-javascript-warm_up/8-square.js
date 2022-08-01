#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    let linea = '';
    for (let a = 0; a < process.argv[2]; a++) {
      linea += 'X';
    }
    console.log(linea);
  }
}
