# https://adventofcode.com/2025/day/2

import os
import re

def part_one(ranges: list[list[int]]):
  invalids: list[int] = []
  for id_range in ranges:
    first, last = id_range
    for id in range(first, last + 1):
      if re.fullmatch(r'(\d+)\1', str(id)):
        invalids.append(id)
  print(sum(invalids))

def part_two(ranges: list[list[int]]):
  invalids: list[int] = []
  for id_range in ranges:
    first, last = id_range
    for id in range(first, last + 1):
      if re.fullmatch(r'(\d+)\1+', str(id)):
        invalids.append(id)
  print(sum(invalids))

def parse(input: str):
  ranges = [[int(id) for id in range.split('-')] for range in input.strip().split(',')]
  return ranges

def read_input(kind: str):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(read_input('example')))
  part_one(parse(read_input('input')))
  part_two(parse(read_input('example')))
  part_two(parse(read_input('input')))
