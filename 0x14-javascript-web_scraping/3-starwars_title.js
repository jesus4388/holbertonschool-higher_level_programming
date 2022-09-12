#!/usr/bin/node
/**
 * prints the title of a Star Wars movie
 *
 */
const url = 'https://swapi-api.hbtn.io/api/films/';
const axios = require('axios').default;

axios.get(url + process.argv[2])
  .then(response => {
  name = response.data;
  console.log(name.title)
  })
  .catch(error => {
  console.log(error);
  });
