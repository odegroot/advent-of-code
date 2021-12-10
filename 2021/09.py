# https://adventofcode.com/2021/day/9

from dataclasses import dataclass
import math
import textwrap

def part_one(heightmap):
  def find_low_point_heights():
    for x in xrange:
      for y in yrange:
        if is_low_point(L(x, y)):
          yield int(heightmap[y][x])

  def is_low_point(l):
    def is_lower(l, n):
      return heightmap[l.y][l.x] < heightmap[n.y][n.x]
    return all(is_lower(l, n) for n in neighbors(l, xrange, yrange))
  
  xrange = range(len(heightmap[0]))
  yrange = range(len(heightmap))

  heights = list(find_low_point_heights())
  risk = sum(h+1 for h in heights)
  print(risk)

def part_two(heightmap):
  def find_basins():
    basins = []
    for x in xrange:
      for y in yrange:
        l = L(x, y)
        if any(l in basin for basin in basins):
          pass
        elif heightmap[l.y][l.x] == '9':
          pass
        else:
          basin = grow_basin(l)
          basins.append(basin)
    return basins

  def grow_basin(l):
    basin = set()
    to_consider = {l}
    while len(to_consider) > 0:
      l = to_consider.pop()
      if l in basin:
        pass
      elif heightmap[l.y][l.x] == '9':
        pass
      else:
        basin.add(l)
        to_consider.update(neighbors(l, xrange, yrange))
    return basin
  
  xrange = range(len(heightmap[0]))
  yrange = range(len(heightmap))

  basins = find_basins()

  sizes = [len(b) for b in basins]
  three_largest = sorted(sizes, reverse=True)[:3]
  print(math.prod(three_largest))

@dataclass(frozen=True)
class L:
  x: int
  y: int

def neighbors(l, xrange, yrange):
  if l.x - 1 in xrange:
    yield L(l.x - 1, l.y)
  if l.x + 1 in xrange:
    yield L(l.x + 1, l.y)
  if l.y - 1 in yrange:
    yield L(l.x, l.y - 1)
  if l.y + 1 in yrange:
    yield L(l.x, l.y + 1)

def parse(input):
  return input.splitlines()

def example_input():
  return textwrap.dedent('''
    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
  '''
  ).strip()

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(example_input()))
  part_two(parse(example_input()))
