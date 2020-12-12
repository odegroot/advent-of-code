function hash(list_size, lengths) {
  let list = [...Array(list_size).keys()];
  let position = 0;
  let skip_size = 0;

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

  return list[0] * list[1];
}

console.log(hash(5, [3, 4, 1, 5]), 'should be 12');
lengths = document.body.innerText.trim().split(',').map(length => Number(length));
console.log(lengths);
console.log(hash(256, lengths));
