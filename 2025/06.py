# https://adventofcode.com/2025/day/6

import math
import os
import re

def part_one(number_lines: list[str], operator_line: str):
  numbers = [[int(number) for number in re.split(r' +', line.strip())] for line in number_lines]
  operators = re.split(r' +', operator_line.strip())
  answers: list[int] = []
  for index, operator in enumerate(operators):
    operands = [row[index] for row in numbers]
    if operator == '+':
      answers.append(sum(operands))
    elif operator == '*':
      answers.append(math.prod(operands))
    else:
      raise Exception(f'Unsupported operator {operator}')
  print(sum(answers))

def part_two(number_lines: list[str], operator_line: str):
  answers: list[int] = []
  operands: list[int] = []
  for index in reversed(range(len(operator_line))):
    operand = ''.join(line[index] for line in number_lines)
    if operand.strip():
      operands.append(int(operand))
    else:
      operands = []
    operator = operator_line[index]
    if operator == ' ':
      pass
    elif operator == '+':
      answers.append(sum(operands))
    elif operator == '*':
      answers.append(math.prod(operands))
    else:
      raise Exception(f'Unsupported operator {operator}')
  print(sum(answers))

def parse(input: str):
  lines = input.splitlines()
  return lines[:-1], lines[-1]

def read_input(kind: str):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(*parse(read_input('example')))
  part_one(*parse(read_input('input')))
  part_two(*parse(read_input('example')))
  part_two(*parse(read_input('input')))
