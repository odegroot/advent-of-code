# https://adventofcode.com/2022/day/2

import os

def part_one(rounds):
  score = 0
  for opponent, you in rounds:
    # A == X == Rock
    # B == Y == Paper
    # C == Z == Scissors
    match you:
      case 'X': score += 1
      case 'Y': score += 2
      case 'Z': score += 3

    if (
      opponent == 'A' and you == 'X' or
      opponent == 'B' and you == 'Y' or
      opponent == 'C' and you == 'Z'
    ):
      score += 3
    elif (
      opponent == 'A' and you == 'Y' or
      opponent == 'B' and you == 'Z' or
      opponent == 'C' and you == 'X'
    ):
      score += 6
    else:
      # opponent == 'A' and you == 'Z' or
      # opponent == 'B' and you == 'X' or
      # opponent == 'C' and you == 'Y'
      score += 0
  print(score)

def part_two(rounds):
  score = 0
  for round in rounds:
    match round:
      case ['A', 'X']: score += 3+0 # R + lose -> choose S
      case ['B', 'X']: score += 1+0 # P + lose -> choose R
      case ['C', 'X']: score += 2+0 # S + lose -> choose P
      case ['A', 'Y']: score += 1+3 # R + draw -> choose R
      case ['B', 'Y']: score += 2+3 # P + draw -> choose P
      case ['C', 'Y']: score += 3+3 # S + draw -> choose S
      case ['A', 'Z']: score += 2+6 # R + win  -> choose P
      case ['B', 'Z']: score += 3+6 # P + win  -> choose S
      case ['C', 'Z']: score += 1+6 # S + win  -> choose R

  print(score)

def parse(input):
  guide = [l.split(' ') for l in input.splitlines()]
  return guide

def read_input(kind):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read().strip()

if __name__ == "__main__":
  part_one(parse(read_input('example')))
  part_one(parse(read_input('input')))
  part_two(parse(read_input('example')))
  part_two(parse(read_input('input')))
