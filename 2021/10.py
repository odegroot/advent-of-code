# https://adventofcode.com/2021/day/10

import math
import textwrap

pairs = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}

def part_one(lines):
  def illegal_chars():
    for line in lines:
      is_corrupt, first_illegal_char = check(line)
      if is_corrupt:
        yield first_illegal_char

  chars = list(illegal_chars())
  scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
  }
  score = sum(scores[char] for char in chars)
  print(score)

def part_two(lines):
  def missing_chars():
    for line in lines:
      is_corrupt, missing = check(line)
      if not is_corrupt:
        yield missing

  def calc_score(completion_string):
    score = 0
    for char in completion_string:
      score *= 5
      score += values[char]
    return score

  completion_strings = list(missing_chars())
  values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
  }
  scores = [calc_score(completion) for completion in completion_strings]
  middle_score = sorted(scores)[math.floor(len(scores)/2)]
  print(middle_score)

def check(line):
  expected = []
  for char in line:
    match char:
      case '(' | '[' | '{' | '<':
        expected.append(pairs[char])
      case ')' | ']' | '}' | '>':
        if expected[-1] == char:
          # valid chunk
          del expected[-1]
        else:
          # corrupt
          return True, char
      case _:
        raise Exception
  return False, ''.join(reversed(expected))

def parse(input):
  return input.splitlines()

def example_input():
  return textwrap.dedent('''
    [({(<(())[]>[[{[]{<()<>>
    [(()[<>])]({[<{<<[]>>(
    {([(<{}[<>[]}>{[]{[(<()>
    (((({<>}<{<{<>}{[]{[]{}
    [[<[([]))<([[{}[[()]]]
    [{[{({}]{}}([{[{{{}}([]
    {<[[]]>}<{[{[{[]{()[[[]
    [<(<(<(<{}))><([]([]()
    <{([([[(<>()){}]>(<<{{
    <{([{{}}[<[[[<>{}]]]>[]]
  '''
  ).strip()

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(example_input()))
  part_two(parse(example_input()))
