# https://adventofcode.com/2020/day/2

import itertools
import operator
import re
import textwrap

def part_one():
  input = [l for l in full_input().strip().splitlines()]
  valid_password_count = sum(is_valid_old(l) for l in input)
  print(valid_password_count)

def is_valid_old(line):
  # 1-3 a: abcde
  min, max, char, password = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
  count = password.count(char)
  # print(min, max, char, password, count)
  return int(min) <= count <= int(max)

def part_two():
  input = [l for l in full_input().strip().splitlines()]
  valid_password_count = sum(is_valid_new(l) for l in input)
  print(valid_password_count)

def is_valid_new(line):
  pos1, pos2, char, password = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
  chars = password[int(pos1)-1] + password[int(pos2)-1]
  count = chars.count(char)
  valid = count == 1
  # print(pos1, pos2, char, password, chars, count, valid)
  return valid

def example_input():
  return textwrap.dedent('''
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
  ''')

def full_input():
  with open('2.input.txt') as f:
    return f.read()

if __name__ == "__main__":
  # part_one()
  part_two()
