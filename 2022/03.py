# https://adventofcode.com/2022/day/3

import os

def part_one(rucksacks):
  def getprio(rucksack):
    size = int(len(rucksack)/2)
    comp1 = rucksack[0:size]
    comp2 = rucksack[size:]
    items1 = set(comp1)
    items2 = set(comp2)
    inboth = items1.intersection(items2).pop()
    if (inboth.islower()):
      return ord(inboth) - ord('a') + 1
    else:
      return ord(inboth) - ord('A') + 27
      
  prios = [getprio(rucksack) for rucksack in rucksacks]
  print(sum(prios))

def part_two(rucksacks):
  groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
  def getprio(group):
    badge = set(group[0]).intersection(group[1]).intersection(group[2]).pop()
    if (badge.islower()):
      return ord(badge) - ord('a') + 1
    else:
      return ord(badge) - ord('A') + 27
      
  prios = [getprio(group) for group in groups]
  print(sum(prios))

def parse(input):
  rucksacks =  input.splitlines()
  return rucksacks

def read_input(kind):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read().strip()

if __name__ == "__main__":
  part_one(parse(read_input('example')))
  part_one(parse(read_input('input')))
  part_two(parse(read_input('example')))
  part_two(parse(read_input('input')))
