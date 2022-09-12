#!/usr/bin/node
/**
 * a script that prints the number of movies
 *
 */
const axion = require('axios').default;
let count = 0;
let datas;
let i;
let url;

axion.get(process.argv[2])
  .then(response => {
    datas = response.data.results;
    for (const dat in datas) {
      url = datas[dat].characters;
      for (i in url) {
        if (url[i].includes(18)) {
          count += 1;
        }
      }
    }
    console.log(count);
  })
  .catch(error => {
    console.log(error);
  });
