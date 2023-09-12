#!/usr/bin/node
exports.esrever = function (list) {
  const retList = [];
  for (let i = list.length; i > 0; i--) {
    retList[list.length - i] = list[i - 1];
  }
  return retList;
};
