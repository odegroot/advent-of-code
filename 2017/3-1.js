// const input = 265149;
// const UP = 1;
// const DOWN = 2;
// const LEFT = 3;
// const RIGHT = 4;

function steps(square) {
  return manhattan_distance(position(square));
}

function position(square) {
  let current_square = 1;
  let current_position = { x: 0, y: 0 };
  let radius = 0;
  let dir = RIGHT;
  while (current_square < square) {
    if (dir === RIGHT) {
      current_square += radius * 2 + 1;
      current_position.x += radius * 2 + 1;
      radius += 1;
      dir = UP;
    } else if (dir === UP) {
      current_square += radius * 2 - 1;
      current_position.y += radius * 2 - 1;
      dir = LEFT;
    } else if (dir === LEFT) {
      current_square += radius * 2;
      current_position.x -= radius * 2;
      dir = DOWN;
    } else if (dir === DOWN) {
      current_square += radius * 2;
      current_position.y -= radius * 2;
      dir = RIGHT;
    }
  }
  if (current_square > square) {
    let diff = current_square - square;
    if (dir === RIGHT) {
      current_position.y += diff;
    } else if (dir === UP) {
      current_position.x -= diff;
    } else if (dir === LEFT) {
      current_position.y -= diff;
    } else if (dir === DOWN) {
      current_position.x += diff;
    }
    current_square -= diff;
  }
  return current_position;
}

function manhattan_distance(position) {
  return Math.abs(position.x) + Math.abs(Math.abs(position.y));
}

console.log(position(12), 'should be (2,  1)');
console.log(position(23), 'should be (0, -2)');
console.log(steps(12), 'should be 3');
console.log(steps(1024), 'should be 31');
console.log(steps(input));
