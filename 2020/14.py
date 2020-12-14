# https://adventofcode.com/2020/day/13

import re

def part_one():
  for input in [example, full_input]:
    mem = {}
    for line in input.splitlines():
      if line.startswith('mask'):
        mask = re.search('[01X]+', line).group(0)
        mask0 = int(mask.replace('X', '1'), 2)
        mask1 = int(mask.replace('X', '0'), 2)
      else:
        addr, val = [int(group) for group in re.fullmatch(r'mem\[(\d+)\] = (\d+)', line).groups()]
        val = val & mask0 | mask1
        mem[addr] = val
    print(sum(mem.values()))

def part_two():
  for input in [example2, full_input]:
    mem = {}
    for line in input.splitlines():
      if line.startswith('mask'):
        mask = re.search('[01X]+', line).group(0)
        mask1 = int(mask.replace('X', '0'), 2)
      else:
        base_addr, val = [int(group) for group in re.fullmatch(r'mem\[(\d+)\] = (\d+)', line).groups()]
        base_addr = base_addr | mask1
        xs = mask.count('X')
        for i in range(2**xs):
          addr = list(format(base_addr, '036b'))
          floatbits = format(i, f'0{xs}b')
          for j, match in enumerate(re.finditer('X', mask)):
            addr[match.start()] = floatbits[j]
          addr = int(''.join(addr), 2)
          mem[addr] = val
    print(sum(mem.values()))

example = '''
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
'''.strip()
example2 = '''
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''.strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
