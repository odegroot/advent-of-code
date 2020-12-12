# https://adventofcode.com/2020/day/11

import copy
import textwrap

def part_one():
  for input in [example, full_input]:
    seats = [list(row) for row in input.splitlines()]
    while True:
      next = do_round_v1(seats)
      if seats == next:
        break
      else:
        seats = next
    occupied = sum([row.count('#') for row in seats])
    print(occupied)
    pass

def do_round_v1(seats):
  def count_8():
    adjacents = []
    start = max(col-1, 0)
    end = col+2
    if row-1 >= 0:
      adjacents += seats[row-1][start:end]
    adjacents += seats[row][col-1] if col > 0 else ''
    adjacents += seats[row][col+1] if col+1 < width else ''
    if row+1 < height:
      adjacents += seats[row+1][start:end]
    return adjacents.count('#')

  next = copy.deepcopy(seats)
  height = len(seats)
  width = len(seats[0])
  for row in range(height):
    for col in range(width):
      if seats[row][col] == '.':
        continue
      adjacent = count_8()
      if adjacent == 0:
        next[row][col] = '#'
      if adjacent >= 4:
        next[row][col] = 'L'
      pass
  return next

def part_two():
  for input, row, col, expected in seatcount_examples():
    seats = [list(row) for row in input.splitlines()]
    print(count_8_v2(seats, row, col), expected)
  for input in [example, full_input]:
    seats = [list(row) for row in input.splitlines()]
    while True:
      next = do_round_v2(seats)
      if seats == next:
        break
      else:
        seats = next
    occupied = sum([row.count('#') for row in seats])
    print(occupied)
    pass

def do_round_v2(seats):
  next = copy.deepcopy(seats)
  for row in range(len(seats)):
    for col in range(len(seats[row])):
      if seats[row][col] == '.':
        continue
      adjacent = count_8_v2(seats, row, col)
      if adjacent == 0:
        next[row][col] = '#'
      if adjacent >= 5:
        next[row][col] = 'L'
      pass
  return next

def count_8_v2(seats, row, col):
  dirs = [
    (-1,-1), (-1, 0), (-1, 1),
    ( 0,-1),          ( 0, 1),
    ( 1,-1), ( 1, 0), ( 1, 1),
  ]
  return sum([count_dir(seats, row, col, d_row, d_col) for d_row, d_col in dirs])

def count_dir(seats, row, col, d_row, d_col):
  if not 0 <= row + d_row < len(seats):
    return 0
  if not 0 <= col + d_col < len(seats[row]):
    return 0
  see = seats[row + d_row][col + d_col]
  if see == '.':
    return count_dir(seats, row + d_row, col + d_col, d_row, d_col)
  elif see == '#':
    return 1
  elif see == 'L':
    return 0
  raise NotImplementedError

example = '''
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''.strip()

def seatcount_examples():
  return [
    (textwrap.dedent('''
      .......#.
      ...#.....
      .#.......
      .........
      ..#L....#
      ....#....
      .........
      #........
      ...#.....
    ''').strip(), 4, 3, 8),
    (textwrap.dedent('''
      .............
      .L.L.#.#.#.#.
      .............
    ''').strip(), 1, 1, 0),
    (textwrap.dedent('''
      .##.##.
      #.#.#.#
      ##...##
      ...L...
      ##...##
      #.#.#.#
      .##.##.
    ''').strip(), 3, 3, 0)
  ]

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

# part_one()
part_two()
