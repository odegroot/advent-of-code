# https://adventofcode.com/2025/day/1

import os

def part_one(rotations):
  dial = 50
  zeroes = 0
  for rotation in rotations:
    dial += rotation
    if dial % 100 == 0:
      zeroes += 1
  print(zeroes)

def part_two(rotations: list[int]):
  dial = 50
  zeroes = 0
  for rotation in rotations:
    for step in range(abs(rotation)):
      if rotation > 0:
        dial += 1
      else:
        dial -= 1
      if dial % 100 == 0:
        zeroes += 1  
  print(zeroes)

def parse(input):
  rotations = [int(rotation.replace('L', '-').replace('R', '')) for rotation in input.splitlines()]
  return rotations

def read_input(kind):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(read_input('example')))
  part_one(parse(read_input('input')))
  part_two(parse(read_input('example')))
  part_two(parse(read_input('input')))
