# https://adventofcode.com/2020/day/8

import copy

def part_one():
  for input in [example, full_input]:
    program = parse(input)
    print(run(program))

def part_two():
  for input in [example, full_input]:
    base_program = parse(input)
    for program in variants(base_program):
      exitcode, accumulator = run(program)
      if exitcode == 'terminated':
        print(accumulator)
        break

def parse(input):
  def parse_line(line):
    op, arg = line.split()
    return [op, int(arg)]
  return [parse_line(line) for line in input.splitlines()]

def run(program):
  accumulator = 0
  ptr = 0
  ptrs_seen = set()
  while True:
    if ptr in ptrs_seen:
      return 'infinite loop', accumulator
    if ptr == len(program):
      return 'terminated', accumulator
    ptrs_seen.add(ptr)

    op, arg = program[ptr]
    if op == 'acc':
      accumulator += arg
      ptr += 1
    elif op == 'jmp':
      ptr += arg
    elif op == 'nop':
      ptr += 1

def variants(program):
  for i in range(len(program)):
    op, arg = program[i]
    if op == 'nop':
      variant = copy.deepcopy(program)
      variant[i][0] = 'jmp'
      yield variant
    elif op == 'jmp':
      variant = copy.deepcopy(program)
      variant[i][0] = 'nop'
      yield variant

example = '''
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''.strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
