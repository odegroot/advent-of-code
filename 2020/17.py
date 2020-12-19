import dataclasses
import operator
import types

def part_one():
  for input in [example, full_input]:
    state = parse(input)
    # pprint(state, 0)
    for cycle in range(1, 7):
      state = do_cycle(state)
      # pprint(state, cycle)
    print(len(state))

def part_two():
  for input in [example, full_input]:
    state = parse4(input)
    # pprint(state, 0)
    for cycle in range(1, 7):
      state = do_cycle4(state)
      # pprint(state, cycle)
    print(len(state))

def parse(input):
  state = set()
  for y, line in enumerate(input.splitlines()):
    for x, cube in enumerate(line):
      if cube == '#':
        state.add(Pos(x, y, 0))
  return state

def parse4(input):
  state = set()
  for y, line in enumerate(input.splitlines()):
    for x, cube in enumerate(line):
      if cube == '#':
        state.add(Pos4(x, y, 0,0))
  return state

def pprint(state, cycle):
  getx = operator.attrgetter('x')
  gety = operator.attrgetter('y')
  getz = operator.attrgetter('z')
  rangex = range(min(state, key=getx).x, max(state, key=getx).x + 1)
  rangey = range(min(state, key=gety).y, max(state, key=gety).y + 1)
  rangez = range(min(state, key=getz).z, max(state, key=getz).z + 1)
  print(f'After {cycle} cycles:\n')
  for z in rangez:
    print(f'z={z}')
    for y in rangey:
      for x in rangex:
        print('#' if Pos(x,y,z) in state else '.', end='')
      print()
    print()

def do_cycle(old):
  new = set()
  to_evaluate = old.copy()
  for pos in old:
    to_evaluate.update(neighbors(pos))
  for pos in to_evaluate:
    active_count = len(old.intersection(neighbors(pos)))
    if active_count == 3:
      new.add(pos)
    elif active_count == 2 and pos in old:
      new.add(pos)
    pass
  return new

def do_cycle4(old):
  new = set()
  to_evaluate = old.copy()
  for pos in old:
    to_evaluate.update(neighbors4(pos))
  for pos in to_evaluate:
    active_count = len(old.intersection(neighbors4(pos)))
    if active_count == 3:
      new.add(pos)
    elif active_count == 2 and pos in old:
      new.add(pos)
    pass
  return new

def neighbors(pos):
  for dx in range(-1, 2):
    for dy in range(-1, 2):
      for dz in range(-1, 2):
        neighbor = Pos(
          pos.x + dx,
          pos.y + dy,
          pos.z + dz,
        )
        if not neighbor == pos:
          yield neighbor
  pass

def neighbors4(pos):
  for dx in range(-1, 2):
    for dy in range(-1, 2):
      for dz in range(-1, 2):
        for dw in range(-1, 2):
          neighbor = Pos4(
            pos.x + dx,
            pos.y + dy,
            pos.z + dz,
            pos.w + dw,
          )
          if not neighbor == pos:
            yield neighbor
  pass

@dataclasses.dataclass(frozen=True)
class Pos:
  x: int
  y: int
  z: int

@dataclasses.dataclass(frozen=True)
class Pos4:
  x: int
  y: int
  z: int
  w: int

example = '''
.#.
..#
###
'''.strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
