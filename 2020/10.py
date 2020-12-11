# https://adventofcode.com/2020/day/10

import collections

def part_one():
  for input in [example, example_2, full_input]:
    ratings = sorted([int(rating) for rating in input.splitlines()])
    ratings = [0] + ratings + [ratings[-1] + 3]
    diffs = [ratings[i] - ratings[i-1] for i in range(1, len(ratings))]
    counts = collections.Counter(diffs)
    print(f'{counts[1]} * {counts[3]} = {counts[1] * counts[3]}')
    pass

def part_two():
  for input in [example, example_2, full_input]:
    ratings = sorted([int(rating) for rating in input.splitlines()])
    ratings = [0] + ratings + [ratings[-1] + 3]
    print(arrangement_count(ratings))

def arrangement_count(ratings, mem={}):
  if count := mem.get(tuple(ratings)):
    return count
  count = 1
  # print(ratings)
  for i in range(len(ratings)-2):
    if ratings[i+2] - ratings[i] <= 3:
      count += arrangement_count([ratings[i]] + ratings[i+2:])
  mem[tuple(ratings)] = count
  return count

example = '''
16
10
15
5
1
11
7
19
6
12
4
'''.strip()
example_2 = '''
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''.strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
