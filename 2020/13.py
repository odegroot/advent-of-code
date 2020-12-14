# https://adventofcode.com/2020/day/13

import itertools

def part_one():
  def departs_in(bus):
    return -depart % bus

  for input in [example, full_input]:
    depart, buses = input.splitlines()
    depart = int(depart)
    buses = [int(bus) for bus in buses.split(',') if bus != 'x']
    first_bus = min(buses, key=departs_in)
    print(first_bus * departs_in(first_bus))
    pass

def part_two():
  def all_match():
    base_minute = constraints[0] * k
    for offset, bus in enumerate(constraints):
      if not bus:
        continue
      if (base_minute + offset) % bus != 0:
        return False
    return True
  
  for buses in examples_2 + [full_input.splitlines()[1]]:
    constraints = {int(bus):offset for offset, bus in enumerate(buses.split(',')) if bus != 'x'}
    t, period = 0,1
    for bus, offset in constraints.items():
      for k in itertools.count():
        if (t + k * period + offset) % bus == 0:
          t = t + k * period
          period = period * bus
          break
    print(t)

example = '''
939
7,13,x,x,59,x,31,19
'''.strip()
examples_2 = [
  '7,13,x,x,59,x,31,19',
  '17,x,13,19',
  '67,7,59,61',
  '67,x,7,59,61',
  '67,7,x,59,61',
  '1789,37,47,1889',
]

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
