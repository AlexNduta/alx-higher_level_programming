#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0){
        module.exports = class Rectangle {}
    }

    this.width = w;
    this.height = h;
  }
}

// export as a module
/*
if (w <= 0 || h <= 0) {
  module.exports = class Rectangle {};
} else {
  module.exports = Rectangle;
} */
