# https://aoc.infi.nl/2022/

import dataclasses
import os

def part_one(instructies):
  eindpos, bezocht = verwerk(instructies)
  
  print(eindpos.lat + eindpos.long)

def part_two(instructies):
  eindpos, bezocht = verwerk(instructies)
  
  maxlat = max(pos.lat for pos in bezocht)
  maxlong = max(pos.long for pos in bezocht)
  grid = [[' '] * (maxlong+1) for _ in range(maxlat+1)]
  for pos in bezocht:
    grid[pos.lat][pos.long] = 'X'
  for row in grid.__reversed__():
    print(''.join(row))

def verwerk(instructies):
  kijkrichting = 0
  pos = Pos(0, 0)
  bezocht = [dataclasses.replace(pos)]

  for wat, hoeveel in instructies:
    match wat:
      case 'draai':
        kijkrichting = (kijkrichting + hoeveel) % 360
      case 'loop':
        dlat, dlong = getdeltas(kijkrichting)
        for _ in range(hoeveel):
          pos.lat += dlat
          pos.long += dlong
          bezocht.append(dataclasses.replace(pos))
      case 'spring':
        dlat, dlong = getdeltas(kijkrichting)
        pos.lat += dlat * hoeveel
        pos.long += dlong * hoeveel
        bezocht.append(dataclasses.replace(pos))
      case _:
        raise Exception('NYI')

  return pos, bezocht

@dataclasses.dataclass
class Pos:
  lat: int
  long: int

def getdeltas(kijkrichting):
  match kijkrichting:
    case 0:
      return  1,  0
    case 45:
      return  1,  1
    case 90:
      return  0,  1
    case 135:
      return -1,  1
    case 180:
      return -1,  0
    case 225:
      return -1, -1
    case 270:
      return  0, -1
    case 315:
      return  1, -1
    case _:
      raise Exception

def parse(input):
  def parseline(line):
    wat, hoeveel = line.split(' ')
    return wat, int(hoeveel)

  instructies = [parseline(line) for line in input.splitlines()]
  return instructies

def read_input(kind):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(read_input('example')))
  part_one(parse(read_input('input')))
  part_two(parse(read_input('example')))
  part_two(parse(read_input('input')))
