# https://adventofcode.com/2022/day/1

import textwrap

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

def example_input():
  return textwrap.dedent('''
    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000
  '''
  )

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(full_input().strip()))
  part_two(parse(full_input().strip()))
