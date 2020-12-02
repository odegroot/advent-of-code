# https://adventofcode.com/2019/day/2

import itertools

def part_one():
  computer = Computer(full_input())
  computer.mem[1] = 12
  computer.mem[2] = 2
  computer.run()
  print(computer.mem[0])

def part_two():
  possible_inputs = itertools.product(range(0,100), repeat=2)
  for (noun, verb) in possible_inputs:
    print(noun, verb)
    computer = Computer(full_input())
    computer.mem[1] = noun
    computer.mem[2] = verb
    computer.run()
    if computer.mem[0] == 19690720:
      break
  print(computer.mem[0], noun, verb, 100 * noun + verb)

class Computer:
  def __init__(self, intcode):
    self.mem = [int(i) for i in intcode.split(',')]
    self.ins_ptr = 0

  def run(self):
    while (opcode := self.mem[self.ins_ptr]) != 99:
      param1, param2, param3 = self.mem[self.ins_ptr+1 : self.ins_ptr+4]
      arg1 = self.mem[param1]
      arg2 = self.mem[param2]
      if opcode == 1:
        result = arg1 + arg2
      elif opcode == 2:
        result = arg1 * arg2
      else:
        raise NotImplementedError(opcode)  
      print(f'{str(self.ins_ptr).rjust(3)}→ [{opcode}, {str(param1).rjust(3)}, {str(param2).rjust(3)}, {str(param3).rjust(3)}] {str(arg1).rjust(7)} {"+" if opcode == 1 else "*"} {str(arg2).rjust(7)} = {str(result).rjust(7)}')
      self.mem[param3] = result
      self.ins_ptr += 4

def example_input():
  return '1,9,10,3,2,3,11,0,99,30,40,50'

def full_input():
  with open('2.input') as f:
    return f.read().strip()

if __name__ == "__main__":
  part_one()
  # part_two()
