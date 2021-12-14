# https://adventofcode.com/2021/day/14

import collections
import re # https://docs.python.org/3/library/re.html

def part_one(polymer, rules):
  def expand(template):
    polymer = template[0]
    for i in range(len(template) - 1):
      pair = template[i:i+2]
      polymer += rules[pair] + template[i+1]
      pass
    return polymer
  
  for _ in range(10):
    polymer = expand(polymer)

  counts = sorted(collections.Counter(polymer).values())
  print(counts[-1] - counts[0])

def part_two(template, rules):
  def expand(paircounts):
    expanded = collections.defaultdict(int)
    for pair, count in paircounts.items():
      mid = rules[pair]
      a = pair[0] + mid
      b = mid + pair[1]
      expanded[a] += count
      expanded[b] += count
    return expanded

  paircounts = collections.defaultdict(int)
  for i in range(len(template) - 1):
    pair = template[i:i+2]
    paircounts[pair] += 1

  for _ in range(40):
    paircounts = expand(paircounts)
  
  elemcounts = collections.defaultdict(int)
  for pair, count in paircounts.items():
    elemcounts[pair[0]] += count
    elemcounts[pair[1]] += count
  # All elements are now counted twice, except for the first and last one.
  elemcounts[template[0]] += 1
  elemcounts[template[-1]] += 1
  counts = sorted(elemcounts.values())
  print((counts[-1] - counts[0])/2)

def parse(input):
  template, rules = input.split('\n\n')
  rules = dict( re.fullmatch(r'(\w\w) -> (\w)', rule).groups() for rule in rules.splitlines() )
  return template, rules

def read_input(kind):
  with open(f'{__file__[-5:-3]}.{kind}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(*parse(read_input('ex')))
  part_two(*parse(read_input('ex')))
