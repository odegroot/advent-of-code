# https://adventofcode.com/2020/day/4

import re

def part_one():
  passports = full_input.split('\n\n')
  valid = [is_valid_lax(passport) for passport in passports]
  print(valid)
  print(sum(valid))

def is_valid_lax(passport):
  actual_fields = re.findall(r'\w\w\w:', passport)
  return set(expected_fields).issubset(actual_fields)

def part_two():
  passports = full_input.split('\n\n')
  print('byr  iyr  eyr  hgt   hcl     ecl pid')
  valid = [is_valid_strict(passport) for passport in passports]
  print(sum(valid))

def is_valid_strict(passport):
  if not is_valid_lax(passport):
    return False
  fields = [entry.split(':') for entry in re.split(r'\s', passport)]
  for field, value in fields:
    if   field == 'byr':
      if not 1920 <= int(value) <= 2002:
        return False
    elif field == 'iyr':
      if not 2010 <= int(value) <= 2020:
        return False
    elif field == 'eyr':
      if not 2020 <= int(value) <= 2030:
        return False
    elif field == 'hgt':
      if not hgt_valid(value):
        return False
    elif field == 'hcl':
      if not re.fullmatch(r'#[0-9a-f]{6}', value):
        return False
    elif field == 'ecl':
      if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    elif field == 'pid':
      if not re.fullmatch(r'\d{9}', value):
        return False
    elif field == 'cid':
      pass
    else:
      raise NotImplementedError(field)
  f = dict(fields)
  print(f'{f["byr"]} {f["iyr"]} {f["eyr"]} {f["hgt"].rjust(5)} {f["hcl"]} {f["ecl"]} {f["pid"]}')
  return True

def hgt_valid(value):
  hgt = int(re.search(r'\d+', value)[0])
  if value[-2:] == 'cm':
    if 150 <= hgt <= 193:
      return True
  elif value[-2:] == 'in':
    if 59 <= hgt <= 76:
      return True
  else:
    return False

expected_fields = set([
  'byr:', # (Birth Year)
  'iyr:', # (Issue Year)
  'eyr:', # (Expiration Year)
  'hgt:', # (Height)
  'hcl:', # (Hair Color)
  'ecl:', # (Eye Color)
  'pid:', # (Passport ID)
  # 'cid:', # (Country ID)
])

example_input= '''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''.strip()

example_two= '''
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
'''.strip()

with open(f'{__file__[-4]}.input') as f:
  full_input = f.read().strip()

part_one()
part_two()
