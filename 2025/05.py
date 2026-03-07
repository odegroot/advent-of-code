# https://adventofcode.com/2025/day/5

import os

def part_one(fresh_ranges: list[range], available_ingredients: list[int]):
  fresh_ingredients = 0
  for id in available_ingredients:
    if any(id in fresh_range for fresh_range in fresh_ranges):
      fresh_ingredients += 1
  print(fresh_ingredients)

def part_two(fresh_ranges: list[range], available_ingredients: list[int]):
  fresh_ranges.sort(key = lambda fresh_range: fresh_range.start)
  deduped_ranges: list[range] = []
  for fresh_range in fresh_ranges:
    for previous in deduped_ranges:
      # Scenario: partial or full overlap → truncate second range
      # =========
      #    ===========
      # or
      # =========
      #   ===
      if previous.stop - 1 >= fresh_range.start:
        fresh_range = range(previous.stop, fresh_range.stop)
    deduped_ranges.append(fresh_range)
  print(sum(len(r) for r in deduped_ranges))

def parse(input: str):
  part1, part2 = input.strip().split('\n\n')
  fresh_ranges: list[range] = []
  for line in part1.splitlines():
    start, end = line.split('-')
    fresh_ranges.append(range(int(start), int(end) + 1))
  available_ingredients = [int(id) for id in part2.splitlines()]
  return fresh_ranges, available_ingredients

def read_input(kind: str):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(*parse(read_input('example')))
  part_one(*parse(read_input('input')))
  part_two(*parse(read_input('example')))
  part_two(*parse(read_input('input')))
