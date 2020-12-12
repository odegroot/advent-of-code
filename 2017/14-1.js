(function () {
"use strict";

function sparse_hash(list_size, lengths) {
  let list = [...Array(list_size).keys()];
  let position = 0;
  let skip_size = 0;

  for (let round = 0; round < 64; round ++) {
    for (let length of lengths) {
      let sublist = [];
      for (let i = position; i < position + length; i++) {
        sublist.push(list[i % list_size]);
      }
      // console.log('sublist is', sublist);
      const reversed = sublist.reverse();

      for (let i = 0; i < length; i++) {
        list[(i + position) % list_size] = reversed[i];
      }
      // console.log('list is now', list);
      position = (position + length + skip_size) % list_size;
      skip_size += 1;
      // console.log(`position = ${position}, skip_size = ${skip_size}`);
    }
  }

  return list;
}

function parse_lengths(input) {
  return [...input].map((char, index) => input.codePointAt(index)).concat(17, 31, 73, 47, 23);
}

function dense_hash(sparse_hash) {
  let dense_hash = [];
  for (let i = 0; i < sparse_hash.length; i += 16) {
    const block = sparse_hash.slice(i, i + 16);
    dense_hash.push(block.reduce((acc, curr) => acc ^ curr));
  }
  return dense_hash;
}

function to_binary(dense_hash) {
  return dense_hash.map(number => number.toString(2).padStart(8, '0')).join('');
}

function knot_hash(input) {
  let lengths = parse_lengths(input);
  let sparse = sparse_hash(256, lengths);
  let dense = dense_hash(sparse);
  return to_binary(dense);
}

// function hex2bin(hex) {
//   let bin = '';
//   for (const char of hex) {
//     // console.log(char);
//     bin += parseInt(char, 16).toString(2).padStart(4, '0');
//     // console.log(bin);
//   }
//   return bin;
// }
// console.log(hex2bin('a0c2017'));
// console.log('10100000110000100000000101110000...');

// console.log(knot_hash('flqrgnkx-0').slice(0, 8).replace(/1/g, '#').replace(/0/g, '.'));
// console.log(knot_hash('flqrgnkx-1').slice(0, 8).replace(/1/g, '#').replace(/0/g, '.'));
// console.log(knot_hash('flqrgnkx-2').slice(0, 8).replace(/1/g, '#').replace(/0/g, '.'));
// console.log(knot_hash('flqrgnkx-3').slice(0, 8).replace(/1/g, '#').replace(/0/g, '.'));
// console.log(knot_hash('flqrgnkx-4').slice(0, 8).replace(/1/g, '#').replace(/0/g, '.'));
// console.log(knot_hash('flqrgnkx-5').slice(0, 8).replace(/1/g, '#').replace(/0/g, '.'));
// console.log(knot_hash('flqrgnkx-6').slice(0, 8).replace(/1/g, '#').replace(/0/g, '.'));
// console.log(knot_hash('flqrgnkx-7').slice(0, 8).replace(/1/g, '#').replace(/0/g, '.'));

function used_squares(input) {
  let used = 0;
  for (let row = 0; row < 128; row += 1) {
    used += knot_hash(`${input}-${row}`).match(/1/g).length;
  }
  return used;
}

let input = 'flqrgnkx';
input = 'hxtvlmkl';
console.log(used_squares(input));

})();
