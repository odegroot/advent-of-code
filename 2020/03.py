# https://adventofcode.com/2020/day/3

import math
import textwrap
import types

def main():
  part_one()
  part_two()

def part_one():
  map = full_input().splitlines()

  slope = (3, 1)
  trees = how_many_trees(map, slope)
  print(trees)

def part_two():
  map = full_input().splitlines()
  slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
  ]
  trees = [how_many_trees(map, slope) for slope in slopes]
  print(math.prod(trees))

def how_many_trees(map, slope):
  height = len(map)
  width = len(map[0])

  curr = Pos(0 ,0)
  trees = 0
  # pylint: disable=no-member
  while curr.down < height:
    if map[curr.down][curr.right % width] == '#':
      trees += 1
    curr.right += slope[0]
    curr.down += slope[1]
  return trees

class Pos(types.SimpleNamespace):
  def __init__(self, right, down):
    super().__init__(right=right, down=down)

def example_input():
  return textwrap.dedent('''
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
  ''').strip()

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read().strip()

if __name__ == "__main__":
  main()
