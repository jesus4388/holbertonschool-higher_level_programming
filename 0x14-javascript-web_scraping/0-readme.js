#!/usr/bin/node
/**
 * leer contenido de un archivo
 *
 */
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (error, datos) => {
  if (error) {
    console.log(error);
  } else {
    console.log(datos);
  }
});
