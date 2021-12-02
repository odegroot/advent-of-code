# https://adventofcode.com/2021/day/1

import itertools
import textwrap

def part_one():
  input = [int(l) for l in full_input().strip().splitlines()]

  count = 0
  for i, depth in enumerate(input):
    if i == 0:
      continue
    if depth > input[i-1]:
      count += 1

  print(count)

def part_two():
  input = [int(l) for l in full_input().strip().splitlines()]

  count = 0
  for i, depth in enumerate(input):
    if i < 3:
      continue
    if depth > input[i-3]:
      count += 1

  print(count)

def example_input():
  return textwrap.dedent('''
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
  '''
  )

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  # part_one()
  part_two()
