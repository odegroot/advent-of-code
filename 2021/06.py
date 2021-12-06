# https://adventofcode.com/2021/day/6

import collections
import textwrap

def part_one(fish):
  counts = collections.Counter(fish)
  for _ in range(0, 80):
    counts = simulate_day(counts)
  print(sum(counts.values()))

def part_two(fish):
  counts = collections.Counter(fish)
  for _ in range(0, 256):
    counts = simulate_day(counts)
  print(sum(counts.values()))

def simulate_day(counts):
  next_day = collections.defaultdict(int)
  for timer, count in counts.items():
    match(timer):
      case 0:
        next_day[6] += count
        next_day[8] += count
      case n:
        next_day[n-1] += count
  return next_day

def parse(input):
  return [int(n) for n in input.split(',')]

def example_input():
  return textwrap.dedent('''
    3,4,3,1,2
  '''
  ).strip()

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(example_input()))
  part_two(parse(full_input()))
