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
      reversed = sublist.reverse();

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
    block = sparse_hash.slice(i, i + 16);
    dense_hash.push(block.reduce((acc, curr) => acc ^ curr));
  }
  return dense_hash;
}

function to_hex(dense_hash) {
  return dense_hash.map(number => number.toString(16).padStart(2, "0")).join('');
}

function knot_hash(input) {
  let lengths = parse_lengths(input);
  let sparse = sparse_hash(256, lengths);
  let dense = dense_hash(sparse);
  return to_hex(dense);
}

// console.log(parse_lengths('1,2,3'), 'should be [49,44,50,44,51,17,31,73,47,23]');
// console.log(dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]), 'should be [64]');
// console.log(to_hex([64, 7, 255]), 'should be 4007ff');
console.log(knot_hash(''), 'should be a2582a3a0e66e6e86e3812dcb672a272', knot_hash('') === 'a2582a3a0e66e6e86e3812dcb672a272');
console.log(knot_hash('AoC 2017'), 'should be 33efeb34ea91902bb2f59c9920caa6cd');
console.log(knot_hash('1,2,3'), 'should be 3efbe78a8d82f29979031a4aa0b16a9d');
console.log(knot_hash('1,2,4'), 'should be 63960835bcdc130f0b66d7ff4f6a5a8e');
input = document.body.innerText.trim();
console.log(knot_hash(input));
