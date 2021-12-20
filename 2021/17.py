# https://adventofcode.com/2021/day/17

import dataclasses
import math
import os
import re # https://docs.python.org/3/library/re.html

def part_one(target_area):
    miny = target_area[2]
    # after the arc, probe will come back to y=0 with v=-v0.
    # after that it will travel v0+1 steps.
    # if v0+1 > miny, then the probe is guaranteed to overshoot the target area.
    v0 = -miny - 1
    apex = v0 * (v0 + 1) / 2 # https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
    print(int(apex))

def part_two(target_area):
    def hits_target(vx, vy):
        x, y = 0, 0
        while not overshoots(x, y):
            if in_target_area(x, y):
                return True
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1
        return False
    
    def overshoots(x, y):
        return x > target_area[1] or y < target_area[2]
    
    def in_target_area(x, y):
        return target_area[0] <= x <= target_area[1] and target_area[2] <= y <= target_area[3]

    trajectories = set()
    # Find minimum horizontal speed to reach target area.
    # https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
    # https://en.wikipedia.org/wiki/Quadratic_formula
    minvx = math.ceil((math.sqrt(target_area[0]*2*4+1) -1)/2)
    vxrange = range(minvx, target_area[1]+1)
    vyrange = range(target_area[2], -target_area[2])
    for vx in vxrange:
        for vy in vyrange:
            if hits_target(vx, vy):
                trajectories.add((vx, vy))
    print(len(trajectories))
    pass

def parse(input):
    target_area = [int(n) for n in re.fullmatch(r'target area: x=([-\d]+)\.\.([-\d]+), y=([-\d]+)\.\.([-\d]+)', input).groups()]
    return target_area

def read_input(kind):
    with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
        return f.read()

if __name__ == "__main__":
    example = 'target area: x=20..30, y=-10..-5'
    part_one(parse(example))
    part_one(parse(read_input('input')))
    part_two(parse(example))
    part_two(parse(read_input('input')))
