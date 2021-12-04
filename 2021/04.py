# https://adventofcode.com/2021/day/4

import itertools
import numpy # https://numpy.org/doc/stable/reference/index.html
import textwrap
from io import StringIO

def part_one(draws, boards):
  drawn, board, _ = who_wins(draws, boards, 0)
  unmarked = numpy.setdiff1d(board.flatten(), drawn)
  print(sum(unmarked), drawn[-1], sum(unmarked) * drawn[-1])

def part_two(draws, boards):
  remaining = boards[:]
  drawn = []
  while len(remaining) > 0:
    drawn, board, i = who_wins(draws, remaining, len(drawn)-1)
    del remaining[i]

  unmarked = numpy.setdiff1d(board.flatten(), drawn)
  print(sum(unmarked), drawn[-1], sum(unmarked) * drawn[-1])

def who_wins(draws, boards, start_at):
  for i in range(start_at, len(draws)):
    drawn = draws[:i+1]
    for j, board in enumerate(boards):
      if has_won(board, drawn):
        return drawn, board, j
  raise Exception

def has_won(board, drawn):
  for line in itertools.chain(board, board.transpose()):
    if set(line).issubset(drawn):
      return True

def parse(input):
  draws, *boards = input.split('\n\n')
  draws  =  numpy.loadtxt(StringIO(draws), dtype=int, delimiter=',')
  boards = [numpy.loadtxt(StringIO(board), dtype=int) for board in boards]

  return draws, boards

def example_input():
  return textwrap.dedent('''
    7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

    22 13 17 11  0
    8  2 23  4 24
    21  9 14 16  7
    6 10  3 18  5
    1 12 20 15 19

    3 15  0  2 22
    9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6

    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
    2  0 12  3  7
  '''
  )

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(*parse(full_input().strip()))
  part_two(*parse(full_input().strip()))
