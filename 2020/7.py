# https://adventofcode.com/2020/day/7

import re

def part_one():
  rules = parse(full_input)
  transitive_containers = set()
  to_evaluate = {'shiny gold'}
  while to_evaluate:
    inner_color = to_evaluate.pop()
    direct_containers = [outer_color for (outer_color, contents) in rules.items() if inner_color in contents.keys()]
    transitive_containers.update(direct_containers)
    to_evaluate.update(direct_containers)
    pass
  print(len(transitive_containers))

def part_two():
  def inner_count(outer_color):
    return sum([count * (1 + inner_count(inner_color)) for inner_color, count in rules[outer_color].items()])

  for input in [example, example_2, full_input]:
    rules = parse(input)
    print(inner_count('shiny gold'))

def parse(input):
  rules = {}
  for line in input.splitlines():
    # >>> re.findall('(\d )?([a-z ]+?) bag', 'light red bags contain 1 bright white bag, 2 muted yellow bags.')
    # [('', 'light red'), ('1 ', 'bright white'), ('2 ', 'muted yellow')]
    # >>> re.findall('(\d )?([a-z ]+?) bag', 'dotted black bags contain no other bags')
    # [('', 'dotted black'), ('', 's contain no other')]
    matches = re.findall(r'(\d )?([a-z ]+?) bag', line)
    outer_color = matches.pop(0)[1]
    rules[outer_color] = {color:int(num) for (num, color) in matches if not num == ''}
  return rules

example = '''
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''.strip()
example_2 = '''
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
'''.strip()

with open(f'{__file__[-4]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
