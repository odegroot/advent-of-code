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

let severity = 0;
const max_depth = Math.max(...Object.keys(scanners));
for (let layer = 0; layer <= max_depth; layer += 1) {
  if (scanners[layer] && scanners[layer].position === 0) {
    severity += layer * scanners[layer].range;
    // console.log(`${layer} BUSTED, severity bumped to ${severity}.`);
  } else {
    // console.log(`${layer} phew`);
  }
  // Now move the scanners.
  for (const scanner of Object.values(scanners)) {
    scanner.position = (scanner.position + 1) % (scanner.range * 2 - 2);
  }
  // console.log('Scanners are now:', '\n' + Object.entries(scanners).map(([layer, scanner]) => `${layer}: ${scanner.position}`).join('\n'));
}
console.log(severity);

})();
