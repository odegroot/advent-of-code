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
    // console.log(`Stepping to ${step} puts me at (${position.x}, ${position.y}).`)
  }
  return position;
}

function manhattan_distance(position) {
  return Math.abs(position.x) + Math.abs(Math.abs(position.y));
}

// console.log(manhattan_distance(follow_path('ne,ne,ne')) / 2, 'should be 3');
// console.log(manhattan_distance(follow_path('ne,ne,sw,sw')) / 2, 'should be 0');
// console.log(manhattan_distance(follow_path('ne,ne,s,s')) / 2, 'should be 2');
// console.log(manhattan_distance(follow_path('se,sw,se,sw,sw')) / 2, 'should be 3');
path = document.body.innerText.trim();
console.log(manhattan_distance(follow_path(path)) / 2);
