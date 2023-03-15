<<<<<<< HEAD

=======
#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

Object.keys(dict).map(function (key, index) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
});

console.log(newDict);
>>>>>>> 4257823b8176f3d9b1b0cc31d22832b83e6c9295
