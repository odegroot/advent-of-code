# https://adventofcode.com/2022/day/4

import os

def part_one(pairs):
  def fully_contains(pair):
    elf1, elf2 = pair
    section1 = set(range(elf1[0], elf1[1]+1))
    section2 = set(range(elf2[0], elf2[1]+1))
    return section1 <= section2 or section2 <= section1

  fully_contained = [fully_contains(pair) for pair in pairs]
  print(sum(fully_contained))

def part_two(pairs):
  def overlaps(pair):
    elf1, elf2 = pair
    section1 = set(range(elf1[0], elf1[1]+1))
    section2 = set(range(elf2[0], elf2[1]+1))
    return len(section1 & section2) >= 1

  overlapping = [overlaps(pair) for pair in pairs]
  print(sum(overlapping))

def parse(input):
  def parsepair(pair):
    return [tuple(int(num) for num in elf.split('-')) for elf in pair.split(',')]

  pairs = [parsepair(pair) for pair in input.splitlines()]
  return pairs

def read_input(kind):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read().strip()

if __name__ == "__main__":
  part_one(parse(read_input('example')))
  part_one(parse(read_input('input')))
  part_two(parse(read_input('example')))
  part_two(parse(read_input('input')))
