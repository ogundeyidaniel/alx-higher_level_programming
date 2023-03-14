#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocur = 0;
  list.forEach(element => {
    ocur += (element === searchElement) ? 1 : 0;
  });
  return ocur;
};
