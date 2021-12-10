# https://adventofcode.com/2021/day/8

import textwrap

def part_one(input):
  def count_unique_lengths(output):
    return len(list(signal for signal in output if len(signal) in [2, 4, 3, 7]))
  unique_lengths = sum(count_unique_lengths(output) for _, output in input)
  print(unique_lengths)

def part_two(input):
  total = sum(decode(*line) for line in input)
  print(total)

def decode(patterns, output):
  # length 2: [1]
  # length 3: [7]
  # length 4: [4]
  # length 5: [2 3 5]
  # length 6: [0 6 9]
  # length 7: [8]
  [one]   = (p for p in patterns if len(p) == 2)
  [seven] = (p for p in patterns if len(p) == 3)
  [four]  = (p for p in patterns if len(p) == 4)
  [eight] = (p for p in patterns if len(p) == 7)
  [three] = (p for p in patterns if len(p) == 5 and set(one).issubset(p))
  twofive = [p for p in patterns if len(p) == 5 and p != three]
  [two]   = (p for p in twofive  if len(set(p).difference(four)) == 3)
  [five]  = (p for p in twofive  if len(set(p).difference(four)) == 2)
  [six]   = (p for p in patterns if len(p) == 6 and not set(one).issubset(p))
  [nine]  = (p for p in patterns if len(p) == 6 and set(four).issubset(p))
  [zero]  = (p for p in patterns if len(p) == 6 and not p in [six, nine])
  mapping = {
    ''.join(sorted(zero)):  '0',
    ''.join(sorted(one)):   '1',
    ''.join(sorted(two)):   '2',
    ''.join(sorted(three)): '3',
    ''.join(sorted(four)):  '4',
    ''.join(sorted(five)):  '5',
    ''.join(sorted(six)):   '6',
    ''.join(sorted(seven)): '7',
    ''.join(sorted(eight)): '8',
    ''.join(sorted(nine)):  '9',
  }
  decoded = int(''.join(mapping[''.join(sorted(p))] for p in output))
  return decoded

def parse(input):
  def parseline(line):
    patterns, output = line.split(' | ')
    patterns = patterns.split(' ')
    output = output.split(' ')
    return patterns, output
  return [parseline(line) for line in input.splitlines()]

def example_input():
  # return 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
  return textwrap.dedent('''
    be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
    fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
    fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
    aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
    fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
    dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
    bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
    egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
    gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
  '''
  ).strip()

def full_input():
  with open(f'{__file__[-5:-3]}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(example_input()))
  part_two(parse(example_input()))
