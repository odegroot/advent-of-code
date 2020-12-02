# https://adventofcode.com/2019/day/3

import copy
import itertools
import textwrap
import types

def part_one():
  spec1, spec2 = full_input().splitlines()
  wire1 = Wire(spec1)
  wire2 = Wire(spec2)

  pairs = itertools.product(wire1.segments, wire2.segments)
  intersections = find_intersections(itertools.islice(pairs, 1, None))
  origin = Pos(0, 0)
  distances = [manhattan_distance(origin, pos) for (_, _, pos) in intersections]
    
  print(min(distances))

def part_two():
  spec1, spec2 = full_input().splitlines()
  wire1 = Wire(spec1)
  wire2 = Wire(spec2)

  pairs = itertools.product(wire1.segments, wire2.segments)
  intersections = list(find_intersections(itertools.islice(pairs, 1, None)))
  distances = [signal_distance(wire1, wire2, *intersection) for intersection in intersections]
    
  print(min(distances))

def manhattan_distance(pos1, pos2):
  return abs(pos1.right - pos2.right) + abs(pos1.up - pos2.up)

def signal_distance(wire1, wire2, seg1, seg2, intersect_pos):
  dist = 0
  for seg in wire1.segments:
    if seg == seg1:
      dist += manhattan_distance(seg.from_, intersect_pos)
      break
    else:
      dist += seg.dist
  for seg in wire2.segments:
    if seg == seg2:
      dist += manhattan_distance(seg.from_, intersect_pos)
      break
    else:
      dist += seg.dist
  return dist

def find_intersections(pairs):
  for seg1, seg2 in pairs:
    if seg1.right_max() < seg2.right_min():
      #  -----
      #          -----
      continue
    if seg2.right_max() < seg1.right_min():
      #          -----
      #  -----
      continue
    if seg1.up_max() < seg2.up_min():
      continue
    if seg2.up_max() < seg1.up_min():
      continue
    
    #  |
    # -+---
    #  | 
    #  |
    right = set(range(seg1.right_min(), seg1.right_max()+1)).intersection(range(seg2.right_min(), seg2.right_max()+1)).pop()
    up =    set(range(seg1.   up_min(), seg1.   up_max()+1)).intersection(range(seg2.   up_min(), seg2.   up_max()+1)).pop()
    yield seg1, seg2, Pos(right, up)

class Wire:
  def __init__(self, wire_spec):
    self.segments = []
    curr = Pos(0, 0)
    print('---')
    for seg_spec in wire_spec.split(','):
      dir = seg_spec[0]
      dist = int(seg_spec[1:])
      # pylint: disable=no-member
      if dir == 'R':
        seg = Segment(curr, Pos(curr.right + dist, curr.up), dist)
        curr.right += dist
      elif dir == 'L':
        seg = Segment(curr, Pos(curr.right - dist, curr.up), dist)
        curr.right -= dist
      elif dir == 'U':
        seg = Segment(curr, Pos(curr.right, curr.up + dist), dist)
        curr.up += dist
      elif dir == 'D':
        seg = Segment(curr, Pos(curr.right, curr.up - dist), dist)
        curr.up -= dist
      self.segments.append(seg)
      print(curr, seg_spec, dir, dist, seg)

class Segment(types.SimpleNamespace):
  def __init__(self, from_, to, dist):
    super().__init__(from_=copy.copy(from_), to=to, dist=dist)
  
  def right_min(self): return min(self.from_.right, self.to.right)
  def right_max(self): return max(self.from_.right, self.to.right)
  def up_min(self):    return min(self.from_.up, self.to.up)
  def up_max(self):    return max(self.from_.up, self.to.up)

class Pos(types.SimpleNamespace):
  def __init__(self, right=0, up=0):
    super().__init__(right=right, up=up)

def example_input():
  return textwrap.dedent('''
    R8,U5,L5,D3
    U7,R6,D4,L4
  ''').strip()

def full_input():
  with open('3.input') as f:
    return f.read().strip()

if __name__ == "__main__":
  # part_one()
  part_two()
