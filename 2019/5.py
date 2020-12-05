# https://adventofcode.com/2019/day/5

import itertools

def part_one():
  Computer(full_input, 1).run()
  # for example in examples:
  #   print(example)
  #   Computer(example, 42).run()

def part_two():
  # for (program, input, expected) in examples_2:
  #   output = Computer(program, input).run()
  #   print(f'{program[:10]}… {input}→{output} ({expected})')
  Computer(full_input, 5).run()

class Computer:
  def __init__(self, intcode, input):
    self.mem = [int(i) for i in intcode.split(',')]
    self.ins_ptr = 0
    self.input = input

  def run(self):
    while self.ins_ptr < len(self.mem):
      op = self.mem[self.ins_ptr]
      opcode = int(str(op)[-2:])
      param_modes = str(op)[:-2]
      if opcode == 1:
        x, y = self.get_vals(2, param_modes)
        dest = self.mem[self.ins_ptr + 3]
        self.mem[dest] = x + y
        self.ins_ptr += 4
      elif opcode == 2:
        x, y = self.get_vals(2, param_modes)
        dest = self.mem[self.ins_ptr + 3]
        self.mem[dest] = x * y
        self.ins_ptr += 4
      elif opcode == 3: # read input
        dest = self.mem[self.ins_ptr + 1]
        self.mem[dest] = self.input
        self.ins_ptr += 2
      elif opcode == 4: # write output
        val, = self.get_vals(1, param_modes)
        self.output = val
        print(f'output {val}')
        self.ins_ptr += 2
      elif opcode == 5: # jump-if-true
        val, ptr = self.get_vals(2, param_modes)
        if val == 0:
          self.ins_ptr += 3
        else:
          self.ins_ptr = ptr
      elif opcode == 6: # jump-if-false
        val, ptr = self.get_vals(2, param_modes)
        if val == 0:
          self.ins_ptr = ptr
        else:
          self.ins_ptr += 3
      elif opcode == 7: # less than
        x, y = self.get_vals(2, param_modes)
        dest = self.mem[self.ins_ptr + 3]
        self.mem[dest] = 1 if x < y else 0
        self.ins_ptr += 4
      elif opcode == 8: # equals
        x, y = self.get_vals(2, param_modes)
        dest = self.mem[self.ins_ptr + 3]
        self.mem[dest] = 1 if x == y else 0
        self.ins_ptr += 4
      elif opcode == 99:
        return self.output
      else:
        raise NotImplementedError(opcode)  
      # print(f'{str(self.ins_ptr).rjust(3)}→ [{opcode}, {str(param1).rjust(3)}, {str(param2).rjust(3)}, {str(param3).rjust(3)}] {str(arg1).rjust(7)} {"+" if opcode == 1 else "*"} {str(arg2).rjust(7)} = {str(result).rjust(7)}')
    print('ran out of instructions')

  def get_vals(self, count, param_modes):
    modes = param_modes.rjust(2, '0')
    get_vals = []
    for i in range(1, count+1):
      mode = modes[-i]
      val = self.mem[self.ins_ptr + i]
      if mode == '0':
        get_vals.append(self.mem[val])
      elif mode == '1':
        get_vals.append(val)
      else:
        raise NotImplementedError
    return get_vals

examples = [
  '3,0,4,0,99',
  '1002,4,3,4,33',
  '1101,100,-1,4,0'
]
examples_2 = [
  # = < pos mode
  ('3,9,8,9,10,9,4,9,99,-1,8', 7, 0),
  ('3,9,8,9,10,9,4,9,99,-1,8', 8, 1),
  ('3,9,8,9,10,9,4,9,99,-1,8', 9, 0),
  ('3,9,7,9,10,9,4,9,99,-1,8', 7, 1),
  ('3,9,7,9,10,9,4,9,99,-1,8', 8, 0),
  ('3,9,7,9,10,9,4,9,99,-1,8', 9, 0),
  # = < imm mode
  ('3,3,1108,-1,8,3,4,3,99', 7, 0),
  ('3,3,1108,-1,8,3,4,3,99', 8, 1),
  ('3,3,1108,-1,8,3,4,3,99', 9, 0),
  ('3,3,1107,-1,8,3,4,3,99', 7, 1),
  ('3,3,1107,-1,8,3,4,3,99', 8, 0),
  ('3,3,1107,-1,8,3,4,3,99', 9, 0),
  # jump
  ('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 0, 0),
  ('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 2, 1),
  ('3,3,1105,-1,9,1101,0,0,12,4,12,99,1',  0, 0),
  ('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', -1, 1),
  # larger
  ('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', 7,  999),
  ('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', 8, 1000),
  ('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', 9, 1001),
]

with open(f'{__file__[-4]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
