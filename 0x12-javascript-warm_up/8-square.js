#!/usr/bin/node

const varg = parseInt(process.argv[2]);

if (isNaN(varg) || varg === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < varg; i++) {
    console.log('x'.repeat(varg));
  }
}
