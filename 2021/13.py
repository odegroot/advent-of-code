# https://adventofcode.com/2021/day/13

import numpy # https://numpy.org/doc/stable/reference/index.html
import re # https://docs.python.org/3/library/re.html

def part_one(dots, folds):
  def do_fold(paper: numpy.ndarray, axis, mid):
    if axis == 'x':
      lefthalf  = paper[:mid,    ...]
      righthalf = paper[:mid:-1, ...]
      return lefthalf | righthalf
    else:
      tophalf    = paper[..., :mid]
      bottomhalf = paper[..., :mid:-1]
      return tophalf | bottomhalf

  cols = max(dot[0] for dot in dots) + 1
  rows = max(dot[1] for dot in dots) + 1
  paper = numpy.zeros(shape=(cols, rows), dtype=bool)
  for dot in dots:
    paper[dot] = True

  for axis, mid in folds:
    paper = do_fold(paper, axis, mid)
    break
  
  count = len(list(dot for dot in paper.flat if dot))
  print(count)

def part_two(dots, folds):
  def do_fold(paper: numpy.ndarray, axis, mid):
    if axis == 'x':
      lefthalf  = paper[:mid,    ...]
      righthalf = paper[:mid:-1, ...]
      return lefthalf | righthalf
    else:
      tophalf    = paper[..., :mid   ]
      bottomhalf = paper[..., :mid:-1]
      to_pad = tophalf.shape[1] - bottomhalf.shape[1]
      bottomhalf = numpy.pad(bottomhalf, ((0, 0), (to_pad, 0)))
      return tophalf | bottomhalf

  cols = max(dot[0] for dot in dots) + 1
  rows = max(dot[1] for dot in dots) + 1
  paper = numpy.zeros(shape=(cols, rows), dtype=bool)
  for dot in dots:
    paper[dot] = True

  for axis, mid in folds:
    paper = do_fold(paper, axis, mid)
  
  print(paper.T.astype(int))

def parse(input):
  def parsefold(line: str):
    axis, coord = re.fullmatch(r'fold along (\w)=(\d+)', line).groups()
    return axis, int(coord)
  section_dots, section_folds = input.split('\n\n')
  dots = [tuple(int(c) for c in line.split(',')) for line in section_dots.splitlines()]
  folds = [parsefold(line) for line in section_folds.splitlines()]
  return dots, folds

def read_input(kind):
  with open(f'{__file__[-5:-3]}.{kind}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(*parse(read_input('ex')))
  part_two(*parse(read_input('full')))
