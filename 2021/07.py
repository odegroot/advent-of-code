# https://adventofcode.com/2021/day/7

import textwrap
import statistics

def part_one(crabs):
  median = int(statistics.median(crabs))
  distances = [abs(p - median) for p in crabs]
  print(sum(distances))

def part_two(crabs):
  p = round(statistics.mean(crabs))
  dist = triangle_distance(crabs, p)
  # hillclimb
  for i in range(p - 1, 0, -1):
    newdist = triangle_distance(crabs, i)
    if newdist < dist:
      p = i
      dist = newdist
    else:
      break
  for i in range(p+1, max(crabs)):
    newdist = triangle_distance(crabs, i)
    if newdist < dist:
      p = i
      dist = newdist
    else:
      break
  print(p, dist)

def triangle_distance(nums, peg):
  def triangle(n):
    return int(n * (n+1) / 2)
  return sum(triangle(abs(n - peg)) for n in nums)

def parse(input):
  return [int(n) for n in input.split(',')]

def example_input():
  return textwrap.dedent('''
    16,1,2,0,4,2,7,1,2,14
  '''
  ).strip()

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(example_input()))
  part_two(parse(example_input()))
