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
lines = input.trim().split('\n');

weights = {};
parents = {};
children = {};
for (let line of lines) {
  weight = Number(line.match(/\d+/)[0]);
  names = line.match(/[a-z]+/g);
  let parent = names[0];
  weights[parent] = weight;
  for (let i = 1; i < names.length; i++) {
    let child = names[i];
    parents[child] = parent;
  }
  children[parent] = names.slice(1);
}
function weight_of(node) {
  weight = weights[node];
  for (let child of children[node]) {
    weight += weight_of(child);
  }
  return weight;
}
function is_balanced(node) {
  let child_weights = children[node].map(child => weight_of(child));
  return child_weights.every(weight => weight === child_weights[0]);
}
root = null;
parent = Object.keys(parents)[0];
while (parent) {
  root = parent;
  parent = parents[root];
}
function deepest_unbalanced(node) {
  for (let child of children[node]) {
    if (!is_balanced(child)) {
      return deepest_unbalanced(child);
    }
  }
  return node;
}
culprit = deepest_unbalanced(root);
child_weights = children[culprit].map(child => weight_of(child));
console.log(child_weights);
console.log(children[culprit]);
to_adjust = children[culprit][4];
console.log(to_adjust);
console.log(weights[to_adjust]);
console.log(weights[to_adjust]-8);