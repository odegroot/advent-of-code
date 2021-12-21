# https://adventofcode.com/2021/day/18

import copy
import dataclasses
import itertools
import math
import os
import typing

def part_one(sfnums):
    finalsum = sfsum(sfnums)
    mag = magnitude(finalsum)
    print(mag, finalsum)

def part_two(sfnums):
    maxmag = 0
    for linepair in itertools.permutations(sfnums, 2):
        sfnum = sfsum(linepair)
        mag = magnitude(sfnum)
        if mag > maxmag:
            maxmag = mag
            biggestpair = linepair
    print(maxmag, biggestpair)
    pass

def parse(input):
    def parse_sfnum(line):
        def parse_pair():
            nonlocal cursor
            match line[cursor]:
                case '[':
                    cursor += 1
                    left = parse_pair()
                    assert line[cursor] == ','
                    cursor += 1
                    right = parse_pair()
                    assert line[cursor] == ']'
                    cursor += 1
                    return Pair(left, right)
                case _:
                    val = int(line[cursor])
                    cursor += 1
                    return Val(val)
        cursor = 0
        return parse_pair()
    sfnums = [parse_sfnum(line) for line in input.splitlines()]
    return sfnums

@dataclasses.dataclass
class Val:
    val: int
    parent: 'Pair'= None

    def __repr__(self) -> str:
        return str(self.val)

    def lval(self) -> 'Val':
        return self
    def rval(self) -> 'Val':
        return self

@dataclasses.dataclass
class Pair:
    lchild: typing.Union[Val, 'Pair']
    rchild: typing.Union[Val, 'Pair']
    parent: 'Pair' = None

    def __post_init__(self):
        self.lchild.parent = self.rchild.parent = self
    def __repr__(self) -> str:
        return f'[{self.lchild},{self.rchild}]'

    def lneigh(self) -> Val:
        if not self.parent:
            return None
        if self.is_left():
            return self.parent.lneigh()
        else:
            return self.parent.lchild.rval()
    def rneigh(self) -> Val:
        if not self.parent:
            return None
        if self.is_left():
            return self.parent.rchild.lval()
        else:
            return self.parent.rneigh()
    def lval(self) -> Val:
        return self.lchild.lval()
    def rval(self) -> Val:
        return self.rchild.rval()
    def is_left(self):
        assert self.parent
        return self.parent.lchild is self

def treewalk(tree, depth=0):
    yield tree, depth
    if isinstance(tree, Pair):
        yield from treewalk(tree.lchild, depth+1)
        yield from treewalk(tree.rchild, depth+1)

def reduce(sfnum):
    def explode(pair: Pair):
        if pair.lneigh():
            pair.lneigh().val += pair.lchild.val
        if pair.rneigh():
            pair.rneigh().val += pair.rchild.val
        zero = Val(0, parent=pair.parent)
        if pair.is_left():
            pair.parent.lchild = zero
        else:
            pair.parent.rchild = zero
    def split(val: Val):
        lval = math.floor(val.val/2)
        rval = math.ceil(val.val/2)
        pair = Pair(Val(lval), Val(rval), parent=val.parent)
        if val.parent.lchild is val:
            val.parent.lchild = pair
        else:
            val.parent.rchild = pair

    while True:
        for pair, depth in treewalk(sfnum):
            if isinstance(pair, Pair) and depth == 4:
                explode(pair)
                break
        else:
            for val, depth in treewalk(sfnum):
                if isinstance(val, Val) and val.val > 9:
                    split(val)
                    break
            else:
                break

def sfsum(sfnums):
    def add(a, b):
        return Pair(copy.deepcopy(a), copy.deepcopy(b))
    total = sfnums[0]
    for sfnum in sfnums[1:]:
        total = add(total, sfnum)
        reduce(total)

    return total

def magnitude(node: Val|Pair):
    if isinstance(node, Val):
        return node.val
    mag = 3*magnitude(node.lchild) + 2*magnitude(node.rchild)
    return mag

def read_input(kind):
    with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
        return f.read()

if __name__ == "__main__":
    part_one(parse(read_input('ex1')))
    for reduce_in, expected in [
        ('[[[[[9,8],1],2],3],4]', '[[[[0,9],2],3],4]'),
        ('[7,[6,[5,[4,[3,2]]]]]', '[7,[6,[5,[7,0]]]]'),
        ('[[6,[5,[4,[3,2]]]],1]', '[[6,[5,[7,0]]],3]'),
        ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'),
        ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'),

        ('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]', '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'),
    ]:
        [sfnum] = parse(reduce_in)
        reduce(sfnum)
        print(repr(sfnum) == expected, reduce_in, expected)
    for sum_in, expected in [
        ('[1,1]\n[2,2]\n[3,3]\n[4,4]', '[[[[1,1],[2,2]],[3,3]],[4,4]]'),
        ('[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]', '[[[[3,0],[5,3]],[4,4]],[5,5]]'),
        ('[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]\n[6,6]', '[[[[5,0],[7,4]],[5,5]],[6,6]]'),
        (read_input('ex2'), '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'),
    ]:
        sfnums = parse(sum_in)
        result = sfsum(sfnums)
        print(repr(result) == expected, expected)
    for mag_in, expected in [
        ('[9,1]', 29),
        ('[1,9]', 21),
        ('[[9,1],[1,9]]', 129),
        ('[[1,2],[[3,4],5]]', 143),
        ('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', 1384),
        ('[[[[1,1],[2,2]],[3,3]],[4,4]]', 445),
        ('[[[[3,0],[5,3]],[4,4]],[5,5]]', 791),
        ('[[[[5,0],[7,4]],[5,5]],[6,6]]', 1137),
        ('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', 3488),
    ]:
        [sfnum] = parse(mag_in)
        result = magnitude(sfnum)
        print(result == expected, mag_in, expected)
    part_one(parse(read_input('ex3')))
    part_one(parse(read_input('input')))

    part_two(parse(read_input('ex3')))
    part_two(parse(read_input('input')))
