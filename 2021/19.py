# https://adventofcode.com/2021/day/19

import itertools
import numpy
import operator
import os
import re
import textwrap

def part_one(reports):
    # for scanner, beacons in reports:
    #     print(len(beacons))
    pass

def part_two(reports):
    pass

def overlaps(beacons1, beacons2):
    def find_rot_trans(pairA, pairB) -> tuple[list, tuple]:
        ''' Takes two pairs of beacons, one pair from scanner A, one pair from scanner B,
            that likely refer to the same two beacons.
            Returns the rotation + translation to convert coordinate space B to coordinate space A.'''
        for rot in rot_matrices: # try each rotation
            # Rotate coordinate space B to space A
            rotatedB = [rotate(b, rot) for b in pairB]
            # Is this a parallel pairwise match?
            offset = diff(pairA[0], rotatedB[0])
            if translate(rotatedB[1], offset) == pairA[1]:
                return rot, offset
            # Is this a diagonal pairwise match?
            offset = diff(pairA[1], rotatedB[0])
            if translate(rotatedB[1], offset) == pairA[0]:
                return rot, offset
            # This rotation is not a match.
        else:
            raise Exception('matching rotation not found')
    for dim in range(3):
        sorted1 = sorted(beacons1, key=operator.itemgetter(dim))
        sorted2 = sorted(beacons2, key=operator.itemgetter(dim))
        distances1 = [(b[dim]-a[dim], a, b) for a,b in zip(sorted1, sorted1[1:])]
        distances2 = [(b[dim]-a[dim], a, b) for a,b in zip(sorted2, sorted2[1:])]
        set1 = set(d for d,a,b in distances1)
        set2 = set(d for d,a,b in distances2)
        overlap = set1 & set2
        if len(overlap) >= 9:
            biggestdist = max(overlap) # smallest chance of accidental equality
            [pair1] = [(a,b) for d,a,b in distances1 if d == biggestdist]
            [pair2] = [(a,b) for d,a,b in distances2 if d == biggestdist]
            return find_rot_trans(pair1, pair2)
    else:
        # beacon sets do not seem to overlap
        return None
def overlap_test(reports):
    beacons0 = reports[0][1]
    beacons1 = reports[1][1]

    # same beacon:
    beacon0 = (-618, -824,-621)
    beacon1 = ( 686,  422, 578)
    offset  = (  68,-1246, -43)
    # b0 = b1*rot + offset
    # b0 - offset = b1*rot
    # (b0 - offset)/rot = b1
    # rot = [[-1, 0, 0], [0, 1, 0], [0, 0, -1]]
    for rot in rot_matrices:
        b1r = rotate(beacon1, rot)
        b1rt = translate(b1r, offset)
        if b1rt == beacon0:
            break
    matches0 = matches1 = ''
    for beacon in beacons1:
        as0 = translate(rotate(beacon, rot), offset)
        if as0 in beacons0:
            matches0 += ','.join(str(c) for c in as0) + '\n'
            matches1 += ','.join(str(c) for c in beacon) + '\n'
    expected0 = textwrap.dedent('''
        -618,-824,-621
        -537,-823,-458
        -447,-329,318
        404,-588,-901
        544,-627,-890
        528,-643,409
        -661,-816,-575
        390,-675,-793
        423,-701,434
        -345,-311,381
        459,-707,401
        -485,-357,347
    ''')
    expected1 = textwrap.dedent('''
        686,422,578
        605,423,415
        515,917,-361
        -336,658,858
        -476,619,847
        -460,603,-452
        729,430,532
        -322,571,750
        -355,545,-477
        413,935,-424
        -391,539,-444
        553,889,-390
    ''')
    assert matches0.strip() == expected0.strip()
    assert matches1.strip() == expected1.strip()

    rot, offset = overlaps(beacons0, beacons1)
    assert rot == [[-1, 0, 0], [0, 1, 0], [0, 0, -1]]
    assert offset == (68,-1246, -43)

    overlapping = [b for b in beacons1 if translate(rotate(b, rot), offset) in beacons0]
    for scannerA, scannerB in itertools.combinations(reports, r=2):
        print(f'Trying scanners {scannerA[0]} and {scannerB[0]}…')
        result = overlaps(scannerA[1], scannerB[1])
        if result:
            print(f'Found overlap between scanners {scannerA[0]} and {scannerB[0]}.')
    pass

def rotate(vector, R):
    return numpy.dot(R, vector)
def rotate_test(reports):
    example5 = [beacons[-1] for scanner, beacons in reports]
    beacon = example5[0]
    all24 = [tuple(rotate(beacon, R)) for R in rot_matrices]
    assert all(e in all24 for e in example5)
    pass
def translate(vector: tuple, offset: tuple) -> tuple:
    return tuple(c + o for c,o in zip(vector, offset))
def diff(beacon1: tuple, beacon2: tuple) -> tuple:
    return tuple(c1 - c2 for c1, c2 in zip(beacon1, beacon2))

def gen_rotmatrices():
    # The 24 distinct 90-degree rotation matrices
    rot_matrices = []
    for rx in range(4):
        for ry in range(4):
            for rz in range(4):
                rotmatrix = gen_rotmatrix(rx, ry, rz)
                if not rotmatrix in rot_matrices:
                    rot_matrices.append(rotmatrix)
    return rot_matrices
def gen_rotmatrix(g, b, a):
    # Generate rotation matrix for the specified 90-degree steps.
    # https://en.wikipedia.org/wiki/Rotation_matrix
    # https://stackoverflow.com/questions/14367330/how-do-i-rotate-a-3d-matrix-by-90-degrees-counterclockwise
    sin = { 0:0, 1:1, 2: 0, 3:-1 } # 90 degree   sine function
    cos = { 0:1, 1:0, 2:-1, 3: 0 } # 90 degree cosine function
    return [
        [cos[a]*cos[b], cos[a]*sin[b]*sin[g]-sin[a]*cos[g], cos[a]*sin[b]*cos[g]+sin[a]*sin[g]],
        [sin[a]*cos[b], sin[a]*sin[b]*sin[g]+cos[a]*cos[g], sin[a]*sin[b]*cos[g]-cos[a]*sin[g]],
        [      -sin[b],        cos[b]*sin[g]              ,        cos[b]*cos[g]              ],
    ]
rot_matrices = gen_rotmatrices()

def parse(input):
    def parsesection(section):
        scannerline, *beaconlines = section.splitlines()
        scanner = int(re.fullmatch(r'--- scanner (\d+) ---', scannerline).groups()[0])
        beacons = [tuple(int(n) for n in line.split(',')) for line in beaconlines]
        return scanner, beacons
    reports = [parsesection(section) for section in input.split('\n\n')]
    return reports

def read_input(kind):
    with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
        return f.read()

if __name__ == "__main__":
    parse(read_input('ex1'))
    rotate_test(parse(read_input('ex2')))
    overlap_test(parse(read_input('ex3')))
    part_one(parse(read_input('input')))

    # part_two(parse(read_input('ex3')))
    # part_two(parse(read_input('input')))
