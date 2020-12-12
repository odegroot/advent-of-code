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

function count_regions(input) {
  let grid = [];
  for (let row = 0; row < 128; row += 1) {
    grid.push(knot_hash(`${input}-${row}`).split(''));
  }
  return mark_regions(grid);
}

function mark_regions(grid) {
  let regions = 0;
  for (const [y, row] of grid.entries()) {
    for (const [x, square] of row.entries()) {
      if (square === '1') {
        // Found a new, previously unmarked region!
        regions += 1;
        console.log(`Marking region ${regions}.`);
        mark_region(x, y, regions, grid);
      } else {
        // Either '0' or a number. Skip this one.
      }
      // if (y === 0) console.log(is_used);
    }
  }
  // print(grid);
  return regions;
}

function mark_region(x, y, value, grid) {
  if (x < 0 || x >= 128 || y < 0 || y >= 128) {
    // console.log(`(${x}, ${y}) Out of bounds.`);
    return;
  } else if (grid[y][x] === '1') {
    // console.log(`(${x}, ${y}) Hit! Marking and examining neighbours.`);
    grid[y][x] = value;
    mark_region(x-1, y, value, grid);
    mark_region(x+1, y, value, grid);
    mark_region(x, y-1, value, grid);
    mark_region(x, y+1, value, grid);
  } else if (grid[y][x] === '0') {
    // console.log(`(${x}, ${y}) Miss.`);
    return;
  } else if (grid[y][x] === value) {
    // console.log(`(${x}, ${y}) Square already marked.`);
  } else {
    throw `(${x}, ${y}) Err wut?`;
  }
}

function print(grid) {
  for (let row = 0; row < 8; row += 1) {
    console.log(grid[row].slice(0, 8).map(square => (square+'').padStart(3, ' ')).join(''));
  }
}

let input = 'flqrgnkx';
input = 'hxtvlmkl';
console.log(count_regions(input));

})();
