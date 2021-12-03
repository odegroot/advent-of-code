# https://adventofcode.com/2021/day/3

import textwrap

def part_one(lines):
  half = len(lines) / 2
  col_sums = [sum(int(bit) for bit in col) for col in zip(*lines)]
  gamma   = ''.join('1' if sum > half else '0' for sum in col_sums)
  epsilon = ''.join('1' if sum < half else '0' for sum in col_sums)

  print(gamma, epsilon, int(gamma, 2), int(epsilon, 2), int(gamma, 2) * int(epsilon, 2))

def part_two(lines):
  o2  = find_rating(lines, mode='o2',  offset=0)
  co2 = find_rating(lines, mode='co2', offset=0)

  print(o2, co2, int(o2, 2), int(co2, 2), int(o2, 2) * int(co2, 2))

def find_rating(lines, mode, offset):
  if len(lines) == 1:
    return lines[0]

  half = len(lines) / 2
  bits = [*zip(*lines)][offset]
  num_ones = sum(int(bit) for bit in bits)
  if mode == 'o2':
    determinant = '1' if num_ones >= half else '0'
  else:
    determinant = '1' if num_ones < half else '0'
  
  subset = [line for line in lines if line[offset] == determinant]
  return find_rating(subset, mode, offset+1)

def example_input():
  return textwrap.dedent('''
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
  '''
  )

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(full_input().strip().splitlines())
  part_two(full_input().strip().splitlines())
