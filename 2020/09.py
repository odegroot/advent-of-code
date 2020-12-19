# https://adventofcode.com/2020/day/9

import itertools

def part_one():
  for input, pa_len in [(example, 5), (full_input, 25)]:
    nums = [int(num) for num in input.splitlines()]
    for i in range(pa_len, len(nums)):
      preamble = nums[i - pa_len : i]
      num = nums[i]
      if not is_valid(num, preamble):
        print(num)
        break

def part_two():
  for input, target in [(example, 127), (full_input, 26134589)]:
    nums = [int(num) for num in input.splitlines()]
    sequence = find_sequence(nums, target)
    s = sorted(sequence)
    print(s[0] + s[-1])

def is_valid(num, preamble):
  for x, y in itertools.combinations(preamble, 2):
    if x + y == num:
      return True
  return False

def find_sequence(nums, target):
  for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
      total += nums[j]
      if total == target:
        return nums[i : j + 1]
      elif total > target:
        break
  raise NotImplementedError

example = '''
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''.strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
