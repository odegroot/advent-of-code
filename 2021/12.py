# https://adventofcode.com/2021/day/12

from collections import defaultdict

def part_one(graph: dict[str, str]):
  def gen_paths(thusfar: list[str]):
    for next in graph[thusfar[-1]]:
      if next == 'end':
        yield thusfar + [next]
      elif next.islower() and next in thusfar:
        pass
      else:
        yield from gen_paths(thusfar + [next])
      
  paths = list(gen_paths(['start']))
  print(len(paths))

def part_two(graph: dict[str, str]):
  def gen_paths(thusfar: list[str]):
    for next in graph[thusfar[-1]]:
      path = thusfar + [next]
      if next == 'end':
        yield path
      elif too_many_small(path):
        pass
      else:
        yield from gen_paths(path)
  def too_many_small(path: list[str]):
    smallcaves = [cave for cave in path if cave.islower()]
    return len(smallcaves) > len(set(smallcaves)) + 1

  paths = list(gen_paths(['start']))
  print(len(paths))

def parse(input):
  graph = defaultdict(list)
  for line in input.splitlines():
    a, b = line.split('-')
    if b != 'start':
      graph[a].append(b)
    if a != 'start' and b != 'end':
      graph[b].append(a)
  return graph

def read_input(kind):
  with open(f'{__file__[-5:-3]}.{kind}.input') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(read_input('ex3')))
  part_two(parse(read_input('ex3')))
