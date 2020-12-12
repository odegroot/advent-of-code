input =`
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
`;
input = document.body.innerText;

parents = {};

lines = input.trim().split('\n');
for (let line of lines) {
  const regex = /[a-z]+/g
  names = line.match(regex);
  let parent = names[0];
  for (let i = 1; i < names.length; i++) {
    let child = names[i];
    parents[child] = parent;
  }
}
node = null;
parent = Object.keys(parents)[0];
while (parent) {
  node = parent;
  parent = parents[node];
}
console.log(node);