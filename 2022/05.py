# https://adventofcode.com/2022/day/5

import os
import re

def part_one(stacks, rearrangement):
  for count, src, dst in rearrangement:
    for _ in range(count):
      crate = stacks[src-1].pop()
      stacks[dst-1].append(crate)
  top_crates = [stack[-1] for stack in stacks]
  print(''.join(top_crates))

def part_two(stacks, rearrangement):
  for count, src, dst in rearrangement:
    to_move = stacks[src-1][-count:]
    stacks[dst-1].extend(to_move)
    del stacks[src-1][-count:]
  top_crates = [stack[-1] for stack in stacks]
  print(''.join(top_crates))

def parse(input):
  starting_stacks, rearrangement_procedure = input.split('\n\n')
  starting_stacks = starting_stacks.splitlines()
  rearrangement_procedure = rearrangement_procedure.splitlines()
  
  stack_numbers = starting_stacks.pop()
  num_stacks = len(re.findall(r'\d+', stack_numbers))
  stacks = [[] for _ in range(num_stacks)]
  for line in reversed(starting_stacks):
    for stack_index in range(num_stacks):
      crate = line[1 + stack_index * 4]
      if (crate != ' '):
        stacks[stack_index].append(crate)

  def parse_rearrangement(line):
    match = re.match(r'move (\d+) from (\d+) to (\d+)', line)
    return [int(group) for group in match.groups()]
  rearrangement = [parse_rearrangement(line) for line in rearrangement_procedure]
  
  return stacks, rearrangement

def read_input(kind):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(*parse(read_input('example')))
  part_one(*parse(read_input('input')))
  part_two(*parse(read_input('example')))
  part_two(*parse(read_input('input')))
