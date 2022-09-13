#!/usr/bin/node
/**
 * a script that computes the number of task completed
 *
 */
const axios = require('axios').default
let data;
let dat;
let dict = {};
let value = 0;
let id = 0;

axios.get(process.argv[2])
  .then(response => {
    data = response.data;
    for (dat in data) {
      if (id != data[dat].userId) {
        value = 0;
	id = data[dat].userId;
      }
      if (data[dat].completed) {
	dict[data[dat].userId] = value += 1;
      }
    }
    console.log(dict)
    })
  .catch(error => {
    console.log(error);
  });
