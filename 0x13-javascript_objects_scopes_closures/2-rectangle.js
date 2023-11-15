#!/usr/bin/node

let w;
let h;
class Rectangle {
    constructor (w, h){
        this.width = w;
        this.height = h;
    }
}

//export as a module
if (w || h <= 0){
    module.exports = class Rectangle {};
} else {
    module.exports = Rectangle;
}
