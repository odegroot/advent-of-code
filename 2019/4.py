# https://adventofcode.com/2019/day/4

import collections

def part_one():
  print(sum([meets_criteria_1(str(pwd)) for pwd in full_input]))

def meets_criteria_1(pwd):
  if len(set(pwd)) == len(pwd):
    return False # no duplicates
  if sorted(pwd) == list(pwd):
    return True
  return False # not ascending

def part_two():
  # for pwd in example_input_2:
  #   print(meets_criteria_2(pwd))
  print(sum([meets_criteria_2(str(pwd)) for pwd in full_input]))

def meets_criteria_2(pwd):
  if sorted(pwd) != list(pwd):
    return False # not ascending
  counts = collections.Counter(pwd).values()
  if 2 in counts:
    return True
  return False

example_input_1 = [
  '111111',
  '223450',
  '123789',
]
example_input_2 = [
  '112233',
  '123444',
  '111122',
]
full_input = range(273025, 767253+1)
# with open(f'{print(__file__[-4])}.input') as f:
#   full_input = f.read().strip()

part_one()
part_two()
