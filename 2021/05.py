# https://adventofcode.com/2021/day/5

from collections import defaultdict
from dataclasses import dataclass
import itertools # https://docs.python.org/3/library/itertools.html
import re # https://docs.python.org/3/library/re.html
import textwrap

def part_one(lines):
  covered = defaultdict(int)
  for line in lines:
    if   line.start.x == line.end.x:
      yrange = sorted([line.start.y, line.end.y])
      for y in range(yrange[0], yrange[1] + 1):
        covered[P(line.start.x, y)] += 1
    elif line.start.y == line.end.y:
      xrange = sorted([line.start.x, line.end.x])
      for x in range(xrange[0], xrange[1] + 1):
        covered[P(x, line.start.y)] += 1
  print(len(list(v for v in covered.values() if v>1)))

def part_two(lines):
  covered = defaultdict(int)
  for line in lines:
    if   line.start.x < line.end.x:
      xrange = range(line.start.x, line.end.x + 1)
    elif line.start.x > line.end.x:
      xrange = range(line.start.x, line.end.x - 1, -1)
    else:
      xrange   = [line.start.x]
      fillvalue = line.start.x
    
    if   line.start.y < line.end.y:
      yrange = range(line.start.y, line.end.y + 1)
    elif line.start.y > line.end.y:
      yrange = range(line.start.y, line.end.y - 1, -1)
    else:
      yrange   = [line.start.y]
      fillvalue = line.start.y

    for x, y in itertools.zip_longest(xrange, yrange, fillvalue=fillvalue):
      covered[P(x, y)] += 1
  print(len(list(v for v in covered.values() if v>1)))

def parse(input):
  def parseline(line):
    x1, y1, x2, y2 = re.fullmatch(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups()
    return Line(P(int(x1), int(y1)), P(int(x2), int(y2)))
  return [parseline(line) for line in input.splitlines()]

@dataclass(frozen=True)
class P:
  x: int
  y: int

@dataclass(frozen=True)
class Line:
  start: P
  end: P

def example_input():
  return textwrap.dedent('''
    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2
  '''
  )

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(example_input().strip()))
  part_two(parse(example_input().strip()))
