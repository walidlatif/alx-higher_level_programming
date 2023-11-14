#!/usr/bin/node

const tab = [];
exports.esrever = function (list) {
  for (let i = 0; i < list.length; i++) {
    tab[i] = list[list.length - i - 1];
  }
  return tab;
};
