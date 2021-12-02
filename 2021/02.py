# https://adventofcode.com/2021/day/2

import itertools
import textwrap

def part_one(input):
  instructions = [parse(line) for line in input.strip().splitlines()]

  horz = depth = 0
  for direction, distance in instructions:
    match direction:
      case 'forward':
        horz += distance
      case 'down':
        depth += distance
      case 'up':
        depth -= distance
      case _:
        raise Exception(direction)

  print(horz, depth, horz*depth)

def part_two(input):
  instructions = [parse(line) for line in input.strip().splitlines()]

  horz = depth = aim = 0
  for direction, distance in instructions:
    match direction:
      case 'forward':
        horz += distance
        depth += aim * distance
      case 'down':
        aim += distance
      case 'up':
        aim -= distance
      case _:
        raise Exception(direction)

  print(horz, depth, horz*depth)

def parse(line):
  elems = line.split(' ')
  elems[1] = int(elems[1])
  return elems

def example_input():
  return textwrap.dedent('''
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
  '''
  )

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  # part_one(full_input())
  part_two(full_input())
