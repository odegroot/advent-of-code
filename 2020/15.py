import re

def part_one():
  for input in examples + [full_input]:
    starting_numbers = [int(i) for i in input.split(',')]
    last_seen = {}
    diff = 0
    for i, n in enumerate(starting_numbers, 1):
      last_seen[n] = i
    for i in range(len(starting_numbers)+1, 2020+1):
      next = diff
      # print(f'{i}→{next}')
      diff = i - last_seen[next] if next in last_seen else 0
      last_seen[next] = i
    print(next)

def part_two():
  for input in examples + [full_input]:
    starting_numbers = [int(i) for i in input.split(',')]
    last_seen = {}
    diff = 0
    for i, n in enumerate(starting_numbers, 1):
      last_seen[n] = i
    for i in range(len(starting_numbers)+1, 30000000+1):
      next = diff
      # print(f'{i}→{next}')
      diff = i - last_seen[next] if next in last_seen else 0
      last_seen[next] = i
    print(next)
  
examples = [
  '0,3,6',
  '1,3,2',
  '2,1,3',
  '1,2,3',
  '2,3,1',
  '3,2,1',
  '3,1,2',
]

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
