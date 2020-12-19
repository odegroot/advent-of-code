# https://adventofcode.com/2020/day/5

import re
import types

def part_one():
  boarding_passes = full_input.splitlines()
  seats = [decode_pass(bp) for bp in boarding_passes]
  highest_id = max([seat.id for seat in seats])
  print(highest_id)

def part_two():
  boarding_passes = full_input.splitlines()
  seats = [decode_pass(bp) for bp in boarding_passes]
  taken = sorted([seat.id for seat in seats])
  # print(taken)
  for i in range(len(taken)):
    if taken[i+1] != taken[i]+1:
      print(taken[i]+1)
      break

def decode_pass(bp):
  row_fb, col_lr = re.fullmatch(r'([FB]{7})([LR]{3})', bp).groups()
  row = int(row_fb.replace('F', '0').replace('B', '1'), 2)
  col = int(col_lr.replace('L', '0').replace('R', '1'), 2)
  # print(f'row {str(row).rjust(3)}, col {col}, id {row*8+col}')
  return Seat(row, col, row*8+col)

class Seat(types.SimpleNamespace):
  def __init__(self, row, col, id):
    super().__init__(row=row, col=col, id=id)

example = '''
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
'''.strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
