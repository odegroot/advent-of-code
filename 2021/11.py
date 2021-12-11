# https://adventofcode.com/2021/day/11

import itertools
import numpy # https://numpy.org/doc/stable/reference/index.html
import textwrap

xrange = yrange = range(0, 10)

def part_one(grid):
  total_flashes = 0
  for _ in range(0, 100):
    grid, flashes = process_step(grid)
    total_flashes += flashes
  print(total_flashes)

def part_two(grid):
  for step in itertools.count(start=1):
    grid, flashes = process_step(grid)
    if flashes == 100:
      break
  print(step)

def process_step(grid):
  def try_flash(loc):
    if newgrid[loc] <= 9:
      return
    if loc in flashed:
      return
    flashed.add(loc)
    for neighbor in neighbors(*loc):
      newgrid[neighbor] += 1
      try_flash(neighbor)

  newgrid = grid.copy()
  newgrid += 1
  flashed = set()
  for loc, _ in numpy.ndenumerate(newgrid):
    try_flash(loc)
  with numpy.nditer(newgrid, op_flags=['readwrite']) as energies:
    for energy in energies:
      if energy > 9:
        energy[...] = 0
  
  return newgrid, len(flashed)

def neighbors(x, y):
  for nx in range(x-1, x+2):
    for ny in range(y-1, y+2):
      if nx in xrange and ny in yrange and not (x, y) == (nx, ny):
        yield (nx, ny)

def parse(input):
  nums = [[int(char) for char in line] for line in input.splitlines()]
  return numpy.array(nums)

def example_input():
  # return textwrap.dedent('''
  #   11111
  #   19991
  #   19191
  #   19991
  #   11111
  # '''
  # ).strip()
  return textwrap.dedent('''
    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526
  '''
  ).strip()

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(example_input()))
  part_two(parse(example_input()))
