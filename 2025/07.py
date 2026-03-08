# https://adventofcode.com/2025/day/7

import os

def part_one(manifold: list[str]):
  start_line = manifold.pop(0)
  tachyon_indices = {start_line.index('S')}
  splits = 0
  for line in manifold:
    for index, char in enumerate(line):
      if char == '^' and index in tachyon_indices:
        tachyon_indices.remove(index)
        tachyon_indices.add(index - 1)
        tachyon_indices.add(index + 1)
        splits += 1
  print(splits)

def part_two(manifold: list[str]):
  start_line = manifold.pop(0)
  timelines = [1 if char == 'S' else 0 for char in start_line]
  for line in manifold:
    for index, char in enumerate(line):
      if char == '^':
        timelines[index - 1] += timelines[index]
        timelines[index + 1] += timelines[index]
        timelines[index] = 0
  print(sum(timelines))

def parse(input: str):
  return input.strip().splitlines()

def read_input(kind: str):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(read_input('example')))
  part_one(parse(read_input('input')))
  part_two(parse(read_input('example')))
  part_two(parse(read_input('input')))
