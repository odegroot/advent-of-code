# https://adventofcode.com/2022/day/6

import os

def part_one(buffer):
  def find_marker():
    for i in range(4, len(buffer)):
      lastfour = buffer[i-4:i]
      is_marker = len(set(lastfour)) == 4
      if is_marker:
        return i
  print(find_marker())

def part_two(buffer):
  def find_marker():
    for i in range(14, len(buffer)):
      lastfour = buffer[i-14:i]
      is_marker = len(set(lastfour)) == 14
      if is_marker:
        return i
  print(find_marker())

def parse(input):
  return input

def read_input(kind):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(read_input('ex1')))
  part_one(parse(read_input('ex2')))
  part_one(parse(read_input('ex3')))
  part_one(parse(read_input('ex4')))
  part_one(parse(read_input('ex5')))
  part_one(parse(read_input('input')))
  part_two(parse(read_input('ex1')))
  part_two(parse(read_input('ex2')))
  part_two(parse(read_input('ex3')))
  part_two(parse(read_input('ex4')))
  part_two(parse(read_input('ex5')))
  part_two(parse(read_input('input')))
