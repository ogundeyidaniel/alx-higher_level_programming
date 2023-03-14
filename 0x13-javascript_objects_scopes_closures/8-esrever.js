#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  while (list.length) {
    rev.push(list.pop());
  }
  return rev;
};
