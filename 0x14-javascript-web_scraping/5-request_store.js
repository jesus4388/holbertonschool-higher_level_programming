#!/usr/bin/node
/**
 *
 *  a script that gets the contents of a webpage
 *
 */
const axios = require('axios').default;
const fs = require('fs');
let datos;

axios.get(process.argv[2])
  .then(response => {
    datos = response.data;
    fs.writeFile(process.argv[3], datos, (error) => {
      if (error) { console.log(error); }
    });
  });
