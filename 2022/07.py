# https://adventofcode.com/2022/day/7

import collections
import os

def part_one(commands):
  tree = buildtree(commands)
  dirsizes = [treesize(contents) for _, contents in iterdirs(tree)]
  smalldirs = [dirsize for dirsize in dirsizes if dirsize <= 100000]
  print(sum(smalldirs))
  
def buildtree(commands):
  def default_factory():
    return collections.defaultdict(default_factory)
  tree = collections.defaultdict(default_factory)
  cwd = []
  for command, args in commands:
    if command == 'cd':
      if args == '/':
        cwd = [args]
      elif args == '..':
        cwd.pop()
      else:
        cwd.append(args)
    elif command == 'ls':
      curdir = tree
      for dir in cwd:
        curdir = curdir[dir]
      for item in args:
        if item[0] == 'dir':
          pass
        else:
          size, filename = item
          curdir[filename] = int(size)
  return tree

def iterdirs(tree):
  for name, value in tree.items():
    if isinstance(value, dict):
      yield name, value
      yield from iterdirs(value)

def treesize(dir):
  def item_size(item):
    if isinstance(item, dict):
      return treesize(item)
    else:
      return item
  item_sizes = [item_size(item) for _, item in dir.items()]
  return sum(item_sizes)

def part_two(commands):
  tree = buildtree(commands)
  dirsizes = {name : treesize(contents) for name, contents in iterdirs(tree)}
  current_free = 70000000 - dirsizes['/']
  to_delete = 30000000 - current_free

  asc = sorted(dirsizes.items(), key=lambda entry: entry[1])
  for name, size in asc:
    if size >= to_delete:
      victim = name, size
      break
  
  print(victim[1]) # not 6600089, too high

def parse(input):
  def parsecommand(command):
    if command.startswith('cd'):
      return tuple(command.split(' '))
    if command.startswith('ls'):
      contents = [tuple(line.split(' ')) for line in command.splitlines()[1:]]
      return 'ls', contents

  commands = [parsecommand(command.strip()) for command in filter(None, input.split('$ '))]
  return commands

def read_input(kind):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  # part_one(parse(read_input('example')))
  # part_one(parse(read_input('input')))
  part_two(parse(read_input('example')))
  part_two(parse(read_input('input')))
