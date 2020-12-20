def part_one():
  for input in [example, full_input]:
    sum = 0
    for line in input.splitlines():
      tokens = iter(line.replace(' ', ''))
      result = evaluate(tokens)
      # print(result)
      sum += result
    print(sum)

def evaluate(tokens):
  val = next(tokens)
  if val == '(':
    val = evaluate(tokens)
  else:
    val = int(val)
  try:
    while True:
      op = next(tokens)
      if op == ')':
        return val

      arg = next(tokens)
      if arg == '(':
        arg = evaluate(tokens)
      else:
        arg = int(arg)

      if op == '+':
        val += arg
      elif op == '*':
        val *= arg
  except StopIteration:
    return val

def part_two():
  for input in [example, full_input]:
    sum = 0
    for line in input.splitlines():
      tokens = iter(line.replace(' ', ''))
      result = eval2(tokens)
      print(result)
      sum += result
    print(sum)

def eval2(tokens):
  val = next(tokens)
  if val == '(':
    val = eval2(tokens)
  else:
    val = int(val)
  try:
    while True:
      op = next(tokens)
      if op == ')':
        return val
      elif op == '*':
        val *= eval2(tokens)
        return val
      elif op == '+':
        arg = next(tokens)
        if arg == '(':
          arg = eval2(tokens)
        else:
          arg = int(arg)
        val += arg

  except StopIteration:
    return val
  raise NotImplementedError

example = '''
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
'''.strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
