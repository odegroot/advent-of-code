import dataclasses
import itertools
import re
import textwrap

def part_one():
  for input in [example, full_input]:
    rules_block, msgs = input.split('\n\n')

    rules = parse(rules_block)
    regex = to_regex(rules, 0)

    count = sum(bool(re.fullmatch(regex, msg)) for msg in msgs.splitlines())
    print(count)
    pass

def parse(rules_block):
  def parse_seq(seq):
    if seq[0] == '"':
      return seq[1]
    else:
      return [int(val) for val in seq.split(' ')]

  rules = {}
  for line in rules_block.splitlines():
    rulenum, spec = line.split((': '))
    rulenum = int(rulenum)
    if '|' in spec:
      left, right = [parse_seq(seq) for seq in spec.split(' | ')]
      reqs = Either(left, right)
    else:
      reqs = parse_seq(spec)
    rules[rulenum] = reqs
    pass
  return rules

def to_regex(rules, num):
  reqs = rules[num]
  if type(reqs) is list:
    return ''.join(to_regex(rules, rule) for rule in reqs)
  elif type(reqs) is str:
    return reqs
  elif type(reqs) is Either:
    regex_left = ''.join(to_regex(rules, rule) for rule in reqs.left)
    regex_right = ''.join(to_regex(rules, rule) for rule in reqs.right)
    return f'({regex_left}|{regex_right})'
  raise NotImplementedError

def part_two():
  for input in [example_2, full_input]:
    rules_block, msgs = input.split('\n\n')

    rules = parse(rules_block)

    # count = sum(is_valid(msg, rules) for msg in msgs.splitlines())
    # print(count)

    rules[8]  = Either([42], [42, 8])
    rules[11] = Either([42, 31], [42, 11, 31])
    count = sum(is_valid(msg, rules) for msg in msgs.splitlines()[2:])
    print(count)

    pass

def is_valid(msg, rules):
  is_match, remaining = matches(iter(msg), 0, rules)
  if is_match:
    try:
      next(remaining)
      print(False, msg, 'unmatched chars at end of msg')
      return False
    except StopIteration:
      print('True ', msg, 'matches')
      return True
  else:
    print(False, msg, 'not a match')
    return False

def matches(chars, rulenum, rules):
  def matches_list(remaining, rulenums):
    for rule in rulenums:
      is_match, remaining = matches(remaining, rule, rules)
      if not is_match:
        return False, remaining
    return True, remaining

  reqs = rules[rulenum]
  if type(reqs) is list:
    return matches_list(chars, reqs)
  elif type(reqs) is Either:
    chars_left, chars_right = itertools.tee(chars)
    left_is_match, remaining_left   = matches_list(chars_left, reqs.left)
    if left_is_match:
      return True, remaining_left
    right_is_match, remaining_right = matches_list(chars_right, reqs.right)
    if right_is_match:
      return True, remaining_right
    return False, chars
  elif type(reqs) is str:
    try:
      return next(chars) == reqs, chars
    except StopIteration:
      return False, chars

  raise NotImplementedError

@dataclasses.dataclass(frozen=True)
class Either:
  left: list
  right: list

example = textwrap.dedent('''
  0: 4 1 5
  1: 2 3 | 3 2
  2: 4 4 | 5 5
  3: 4 5 | 5 4
  4: "a"
  5: "b"

  ababbb
  bababa
  abbbab
  aaabbb
  aaaabbb
''').strip()
example_2 = textwrap.dedent('''
  42: 9 14 | 10 1
  9: 14 27 | 1 26
  10: 23 14 | 28 1
  1: "a"
  11: 42 31
  5: 1 14 | 15 1
  19: 14 1 | 14 14
  12: 24 14 | 19 1
  16: 15 1 | 14 14
  31: 14 17 | 1 13
  6: 14 14 | 1 14
  2: 1 24 | 14 4
  0: 8 11
  13: 14 3 | 1 12
  15: 1 | 14
  17: 14 2 | 1 7
  23: 25 1 | 22 14
  28: 16 1
  4: 1 1
  20: 14 14 | 1 15
  3: 5 14 | 16 1
  27: 1 6 | 14 18
  14: "b"
  21: 14 1 | 1 14
  25: 1 1 | 1 14
  22: 14 14
  8: 42
  26: 14 22 | 1 20
  18: 15 15
  7: 14 5 | 1 21
  24: 14 1

  abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
  bbabbbbaabaabba
  babbbbaabbbbbabbbbbbaabaaabaaa
  aaabbbbbbaaaabaababaabababbabaaabbababababaaa
  bbbbbbbaaaabbbbaaabbabaaa
  bbbababbbbaaaaaaaabbababaaababaabab
  ababaaaaaabaaab
  ababaaaaabbbaba
  baabbaaaabbaaaababbaababb
  abbbbabbbbaaaababbbbbbaaaababb
  aaaaabbaabaaaaababaa
  aaaabbaaaabbaaa
  aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
  babaaabbbaaabaababbaabababaaab
  aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
''').strip()

with open(f'{__file__[-5:-3]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
