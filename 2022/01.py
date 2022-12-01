# https://adventofcode.com/2022/day/1

import os

def part_one(elves):
  elf_calories = [sum(items) for items in elves]
  print(max(elf_calories))

def part_two(elves):
  elf_calories = [sum(items) for items in elves]
  elf_calories.sort()
  top_three = elf_calories[-3:]
  print(sum(top_three))

def parse(input):
  elf_blocks = input.split('\n\n')
  elves = [[int(l) for l in elf_block.splitlines()] for elf_block in elf_blocks]
  return elves

def read_input(kind):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(read_input('input')))
  part_two(parse(read_input('input')))
