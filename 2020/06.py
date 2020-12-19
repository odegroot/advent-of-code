# https://adventofcode.com/2020/day/6

import re
import types

def part_one():
  for example in [example_1, example_2, full_input]:
    groups = example.split('\n\n')
    total = sum([group_count_1(group) for group in groups])
    print(total)
    # for group in groups:
    #   letters = set(group.replace('\n', ''))
    #   # people = group.splitlines()
    #   print(letters)
    # print('---')

def group_count_1(group):
  return len(set(group.replace('\n', '')))

def part_two():
  for example in [example_2, full_input]:
    groups = example.split('\n\n')
    total = sum([group_count_2(group) for group in groups])
    print(total)

def group_count_2(group):
  people = [set(person) for person in group.splitlines()]
  collectively = people[0].intersection(*people[1:])
  return len(collectively)

example_1 = '''
abcx
abcy
abcz
'''.strip()
example_2 = '''
abc

a
b
c

ab
ac

a
a
a
a

b
'''.strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
