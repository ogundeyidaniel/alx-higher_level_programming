#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let times = 0; times < x; times++) {
    theFunction();
  }
};
