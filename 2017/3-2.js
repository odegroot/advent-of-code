// const input = 265149;
// const UP = 1;
// const DOWN = 2;
// const LEFT = 3;
// const RIGHT = 4;

function fill_squares() {
  let position = { x: 0, y: 0 };
  let radius = 0;
  let dir = RIGHT;
  let last_value_written = 0;
  let grid = { '(0, 0)': 1 };
  while (last_value_written < input) {
    if (dir === RIGHT) {
      position.x += 1;
      if (position.x === radius + 1) {
        radius += 1;
        dir = UP;
      }
    } else if (dir === UP) {
      position.y += 1;
      if (position.y === radius) {
        dir = LEFT;
      }
    } else if (dir === LEFT) {
      position.x -= 1;
      if (position.x === -radius) {
        dir = DOWN;
      }
    } else if (dir === DOWN) {
      position.y -= 1;
      if (position.y === -radius) {
        dir = RIGHT;
      }
    }
    let value = 0;
    value += grid[`(${position.x - 1}, ${position.y + 1})`] || 0;
    value += grid[`(${position.x    }, ${position.y + 1})`] || 0;
    value += grid[`(${position.x + 1}, ${position.y + 1})`] || 0;

    value += grid[`(${position.x - 1}, ${position.y    })`] || 0;
    value += grid[`(${position.x + 1}, ${position.y    })`] || 0;

    value += grid[`(${position.x - 1}, ${position.y - 1})`] || 0;
    value += grid[`(${position.x    }, ${position.y - 1})`] || 0;
    value += grid[`(${position.x + 1}, ${position.y - 1})`] || 0;
    grid[`(${position.x}, ${position.y})`] = value;
    last_value_written = value;
    console.log(position, last_value_written);
  }
  return last_value_written;
}

fill_squares();
