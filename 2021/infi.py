# https://aoc.infi.nl/

import os
import time

def part_one(speelgoed):
  aantallen = [tel_onderdelen(o, speelgoed) for o in speelgoed.values()]
  print(max(aantallen))

def part_two(cadeaus, missend, speelgoed):
  def is_geen_onderdeel(naam):
    return all(naam not in onderdelen for onderdelen in speelgoed.values())
  
  aantallen = dict((tel_onderdelen(o, speelgoed), naam) for naam, o in speelgoed.items() if is_geen_onderdeel(naam))
  minpts = min(aantallen)
  maxpts = max(aantallen)
  seen = set()
  
  def gen_options(rem_parts, rem_picks):
    if (rem_picks, rem_parts) in seen:
      return
    seen.add((rem_picks, rem_parts))
    if rem_picks == 1:
      if rem_parts in aantallen:
        yield [aantallen[rem_parts][0]]
    else:
      rem_avg = rem_parts / rem_picks
      if minpts <= rem_avg <= maxpts:
        for num, name in aantallen.items():
          for subsolution in gen_options(rem_parts - num, rem_picks - 1):
            yield [name[0]] + subsolution

  start = time.time()
  solution = next(gen_options(missend, cadeaus))
  answer = ''.join(sorted(solution))
  end = time.time()
  print(answer, end-start)


def tel_onderdelen(onderdelen, speelgoed):
  sum = 0
  for naam, aantal in onderdelen.items():
    if naam in speelgoed:
      mult = tel_onderdelen(speelgoed[naam], speelgoed)
    else:
      mult = 1
    sum += aantal * mult
  return sum

def parse(input):
  def parseline(line):
    naam, onderdelen = line.split(': ')
    onderdelen = dict(parseonderdeel(o) for o in onderdelen.split(', '))
    return naam, onderdelen
  def parseonderdeel(onderdeel):
    aantal, naam = onderdeel.split(' ')
    return naam, int(aantal)

  missend, *speelgoed = input.splitlines()
  missend = int(missend.split(' ')[0])
  speelgoed = dict(parseline(line) for line in speelgoed)
  return missend, speelgoed

def read_input(kind):
  with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
    return f.read()

if __name__ == "__main__":
  part_one(parse(read_input('example'))[1])
  part_two( 3, *parse(read_input('example')))
  part_two(20, *parse(read_input('input')))
