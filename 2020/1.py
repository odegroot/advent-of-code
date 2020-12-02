# https://adventofcode.com/2020/day/1

import itertools
import textwrap

def part_one():
  input = sorted([int(l) for l in full_input().strip().splitlines()])
  for l in input:
    complement = 2020 - l
    if complement in input:
      break
  print(l * complement)

def part_two():
  input = sorted([int(l) for l in full_input().strip().splitlines()])
  combos = itertools.combinations(input, 2)
  for (n, m) in combos:
    complement = 2020 - n - m
    if complement in input:
      break
  print(n * m * complement)

def example_input():
  return textwrap.dedent('''
    1721
    979
    366
    299
    675
    1456
  ''')

def full_input():
  with open('1.input') as f:
    return f.read()

if __name__ == "__main__":
  # part_one()
  part_two()
