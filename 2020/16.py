import math
import re

def part_one():
  for input in [example, full_input]:
    rules, yourticket, nearbytickets = parse(input)
    
    acceptable_values = set()
    for s in rules.values():
      acceptable_values.update(s)

    error_rate = 0
    for ticket in nearbytickets:
      for value in ticket:
        if value not in acceptable_values:
          error_rate += value
    
    print(error_rate)

def parse(input):
  def parseints(line):
    return [int(value) for value in line.split(',')]

  ruleblock, yourticket, nearbytickets = input.split('\n\n')

  rulelines = ruleblock.splitlines()
  ruleitems = [re.fullmatch(r'([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)', rule).groups() for rule in rulelines]
  rules = {field:{*range(int(r1s), int(r1e)+1), *range(int(r2s), int(r2e)+1)} for field, r1s, r1e, r2s, r2e in ruleitems}

  yourticket = parseints(yourticket.splitlines()[1])

  nearbytickets = [parseints(line) for line in nearbytickets.splitlines()[1:]]
  
  return rules, yourticket, nearbytickets

def part_two():
  def is_valid(ticket):
    return all([value in acceptable_anywhere for value in ticket])

  def possible_positions(acceptable_values):
    return {pos for pos, values in enumerate(pos_values) if values.issubset(acceptable_values)}

  for input in [example, example_2, full_input]:
    rules, yourticket, nearbytickets = parse(input)
    
    acceptable_anywhere = set()
    for s in rules.values():
      acceptable_anywhere.update(s)

    valid_nearby_tickets = list(filter(is_valid, nearbytickets))
    pos_values = [set(values) for values in zip(*valid_nearby_tickets)]
    possible_field_positions = {field:possible_positions(acceptable_values) for field, acceptable_values in rules.items()}

    sorted_fields = sorted(possible_field_positions.items(), key=lambda kvp: len(kvp[1]))
    field_positions = {}
    for i, (field, [position]) in enumerate(sorted_fields):
      field_positions[field] = position
      for (_, positions) in sorted_fields[i+1:]:
        positions.discard(position)

    product = math.prod(yourticket[pos] for field, pos in field_positions.items() if field.startswith('departure'))
    print(product)

example = '''
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
'''.strip()
example_2 = '''
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
'''.strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
