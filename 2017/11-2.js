/*
  x x x
   x x
  x x x
   x x
  x x x

  x   x   x
    x   x
  x   x   x
    x   x
  x   x   x

             xx
            xoox
        xx   xx   xx
       xoox      xoox
   xx   xx   xx   xx   xx
  xoox      xoox      xoox
   xx   xx   xx   xx   xx
       xoox      xoox
        xx   xx   xx
            xoox
             xx

               xx
              xoox
         xx    xx    xx
        xoox        xoox
   xx    xx    xx    xx    xx
  xoox        xoox        xoox
   xx    xx    xx    xx    xx
        xoox        xoox
         xx    xx    xx
              xoox
               xx
*/

function follow_path(path) {
  let steps = path.split(',');

  let position = { x: 0, y: 0 };
  let max_distance = 0;
  for (let step of steps) {
    if (step === 'n') {
      position.y += 2;
    } else if (step === 'ne') {
      position.x += 1;
      position.y += 1;
    } else if (step === 'se') {
      position.x += 1;
      position.y -= 1;
    } else if (step === 's') {
      position.y -= 2;
    } else if (step === 'sw') {
      position.x -= 1;
      position.y -= 1;
    } else if (step === 'nw') {
      position.x -= 1;
      position.y += 1;
    } else {
      throw 'wtf';
    }
    let distance = manhattan_distance(position) / 2;
    if (distance > max_distance) {
      max_distance = distance;
    }
    // console.log(`Stepping to ${step} puts me at (${position.x}, ${position.y}).`)
  }
  return max_distance;
}

function manhattan_distance(position) {
  return Math.abs(position.x) + Math.abs(Math.abs(position.y));
}

path = document.body.innerText.trim();
console.log(follow_path(path));
