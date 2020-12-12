(function () {
"use strict";

let input = `
0: 3
1: 2
4: 4
6: 4
`.trim();
input = document.body.innerText.trim();

const scanners = {};
const lines = input.split('\n');

for (const line of lines) {
  const [depth, range] = line.match(/\d+/g).map(Number);
  scanners[depth] = {
    position: 0,
    range,
  };
  // console.log(line, depth, range, scanners);
}
const max_depth = Math.max(...Object.keys(scanners));

function gets_caught(scanners)   {
  // console.log("Let's try with this setup.", '\n' + Object.entries(scanners).map(([layer, scanner]) => `${layer}: ${scanner.position}`).join('\n'));
  for (let [depth, scanner] of Object.entries(scanners)) {
    depth = Number(depth);
    if ((scanner.position + depth) % (scanner.range * 2 - 2) === 0) {
      // console.log(`BUSTED at depth ${depth}!`);
      return true;
    } else {
      // console.log(`Phew, we're at depth ${depth}, but luckily the scanner is at position ${(scanner.position + depth) % (scanner.range * 2 - 2)}.`)
    }
  }
  return false;
}

function move_scanners(scanners) {
  for (const scanner of Object.values(scanners)) {
    scanner.position = (scanner.position + 1) % (scanner.range * 2 - 2);
  }
}

let delay = 0;
while (gets_caught(scanners)) {
  if (delay % 1000 === 0) console.log(`A delay of ${delay} gets me caught. :'(`);
  delay += 1;
  move_scanners(scanners);
}
console.log(delay);

})();
