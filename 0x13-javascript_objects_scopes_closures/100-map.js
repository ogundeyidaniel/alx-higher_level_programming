#!/usr/bin/node
const firstList = require('./100-data').list;
const secondList = firstList.map((value, index) => value * index);
console.log(firstList);
console.log(secondList);
