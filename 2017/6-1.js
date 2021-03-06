function reallocate(banks) {
  let redistributions = 0;
  let seen_configurations = new Set();
  let length = banks.length;

  while (!seen_configurations.has(banks.join(' '))) {
    seen_configurations.add(banks.join(' '));

    let max = Math.max(...banks);
    let index = banks.indexOf(max);
    // console.log(`Configuration is ${banks.join(' ')}. Redistributing the blocks in bank ${index}, which has ${max} blocks.`);
    banks[index] = 0;
    for (let i = 1; i <= max; i++) {
      banks[(index + i) % length] += 1;
    }
    redistributions += 1;
  }
  return redistributions;
}

console.log(reallocate([0, 2, 7, 0]), 'should be 5');
let input = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6];
console.log(reallocate(input));
