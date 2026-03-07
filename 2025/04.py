# https://adventofcode.com/2025/day/4

import os

def part_one(grid: list[list[str]]):
  accessible_rolls = 0
  for row, line in enumerate(grid):
    for column, paper in enumerate(line):
      if paper == '.':
        pass
      elif paper == '@':
        adjacent_rolls = get_adjacent_rolls(row, column, grid)
        if adjacent_rolls < 4:
          accessible_rolls += 1
      else:
        raise Exception('blorb invalid value')
  print(accessible_rolls)

def get_adjacent_rolls(row: int, column: int, grid: list[list[str]]):
  rolls = 0
  for r in range(row - 1, row + 2):
    for c in range(column - 1, column + 2):
      if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and not(r == row and c == column):
        if grid[r][c] == '@':
          rolls += 1
  return rolls

def part_two(grid: list[list[str]]):
  rolls_removed = 0
  check_again = True
  while check_again:
    check_again = False
    for row, line in enumerate(grid):
      for column, paper in enumerate(line):
        if paper == '.':
          pass
        elif paper == '@':
          adjacent_rolls = get_adjacent_rolls(row, column, grid)
          if adjacent_rolls < 4:
            grid[row][column] = '.'
            rolls_removed += 1
            check_again = True
        else:
          raise Exception('blorb invalid value')
  print(rolls_removed)

def parse(input: str):
  grid = [list(line) for line in input.strip().splitlines()]
  return grid

def read_input(kind: str):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(read_input('example')))
  part_one(parse(read_input('input')))
  part_two(parse(read_input('example')))
  part_two(parse(read_input('input')))
