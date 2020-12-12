# https://adventofcode.com/2020/day/12

# https://developercommunity.visualstudio.com/content/problem/1207405/fmod-after-an-update-to-windows-2004-is-causing-a.html?page=3&pageSize=10&sort=votes&type=problem
import numpy # pip install numpy==1.19.3

NORTH = numpy.array([ 0, 1])
EAST  = numpy.array([ 1, 0])
SOUTH = numpy.array([ 0,-1])
WEST  = numpy.array([-1, 0])
dirs = [NORTH, EAST, SOUTH, WEST]

def part_one():
  for input in [example, full_input]:
    pos = numpy.array([0, 0])
    facing = 1 # EAST
    for line in input.splitlines():
      action = line[0]
      arg = int(line[1:])
      if   action == 'N':
        pos += NORTH * arg
      elif action == 'E':
        pos += EAST * arg
      elif action == 'S':
        pos += SOUTH * arg
      elif action == 'W':
        pos += WEST * arg
      elif action == 'L':
        facing = (facing - arg // 90) % 4
      elif action == 'R':
        facing = (facing + arg // 90) % 4
      elif action == 'F':
        pos += dirs[facing] * arg
      else:
        raise NotImplementedError
    manhattan = sum([abs(c) for c in pos])
    print(manhattan)

def part_two():
  for input in [example, full_input]:
    pos = numpy.array([0, 0])
    waypoint = numpy.array([10, 1])
    for line in input.splitlines():
      action = line[0]
      arg = int(line[1:])
      if   action == 'N':
        waypoint += NORTH * arg
      elif action == 'E':
        waypoint += EAST * arg
      elif action == 'S':
        waypoint += SOUTH * arg
      elif action == 'W':
        waypoint += WEST * arg
      elif action == 'L':
        waypoint = rotate(waypoint, -arg)
      elif action == 'R':
        waypoint = rotate(waypoint, arg)
      elif action == 'F':
        pos += waypoint * arg
      else:
        raise NotImplementedError
    manhattan = sum([abs(c) for c in pos])
    print(manhattan)

def rotate(waypoint, deg):
  steps = deg // 90 % 4
  if steps == 1:
    return numpy.array([waypoint[1], -waypoint[0]])
  if steps == 2:
    return -waypoint
  if steps == 3:
    return numpy.array([-waypoint[1], waypoint[0]])


example = '''
F10
N3
F7
R90
F11
'''.strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
