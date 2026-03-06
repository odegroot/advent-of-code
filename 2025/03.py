# https://adventofcode.com/2025/day/3

import os

def part_one(banks: list[str]):
  joltages: list[int] = []
  for bank in banks:
    index_tens = max(range(len(bank)-1), key=bank.__getitem__)
    tens = bank[index_tens]
    singles = max(bank[index_tens+1:])
    joltages.append(int(tens + singles))
  print(sum(joltages))

def part_two(banks: list[str]):
  joltages: list[int] = []
  for bank in banks:
    joltage = ''
    start_index = 0
    for batnum in range(12):
      end_index = len(bank) - (11-batnum)
      index_max = max(range(start_index, end_index), key=bank.__getitem__)
      joltage += bank[index_max]
      start_index = index_max + 1
    joltages.append(int(joltage))
  print(sum(joltages))

def parse(input: str):
  banks = input.strip().splitlines()
  return banks

def read_input(kind: str):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(read_input('example')))
  part_one(parse(read_input('input')))
  part_two(parse(read_input('example')))
  part_two(parse(read_input('input')))
