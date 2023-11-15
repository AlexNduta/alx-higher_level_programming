#!/usr/bin/node

const rec = require('./4-rectangle.js');

module.exports = class Square extends rec {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
};
