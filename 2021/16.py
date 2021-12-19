# https://adventofcode.com/2021/day/16

import dataclasses
import math
import os

def part_one(packet):
    def versionsum(packet: Packet):
        return packet.version + sum(versionsum(p) for p in packet.subpackets)

    print(versionsum(packet))


def part_two(packet):
    def val(packet: Packet):
        subpack_vals = [val(p) for p in packet.subpackets]
        match packet.type:
            case 0:
                return sum(subpack_vals)
            case 1:
                return math.prod(subpack_vals)
            case 2:
                return min(subpack_vals)
            case 3:
                return max(subpack_vals)
            case 4:
                return packet.litval
            case 5:
                return int(subpack_vals[0] > subpack_vals[1])
            case 6:
                return int(subpack_vals[0] < subpack_vals[1])
            case 7:
                return int(subpack_vals[0] ==subpack_vals[1])
    
    outer_val = val(packet)
    print(outer_val)

@dataclasses.dataclass(frozen=True)
class Packet:
  version: int
  type: int
  litval: int = -1
  subpackets: list = dataclasses.field(default_factory=list)

def parse(hex):
    i = int(hex, 16)
    bits = format(i, f'0>{len(hex)*4}b')
    cursor = 0
    def read_s(count):
        nonlocal cursor
        val = bits[cursor:cursor+count]
        cursor += count
        return val
    def read_i(count):
        return int(read_s(count), 2)
    def read_packet():
        pversion = read_i(3)
        ptype = read_i(3)
        match ptype:
            case 4: # literal value
                litval = read_litval()
                return Packet(pversion, ptype, litval=litval)
            case _: # operator packet
                oppack = read_op_pack()
                return Packet(pversion, ptype, subpackets=oppack)
    def read_litval():
        hasmore = 1
        litvalbits = ''
        while hasmore:
            hasmore = read_i(1)
            litvalbits += read_s(4)
        return int(litvalbits, 2)
    def read_op_pack():
        lentype = read_i(1)
        match lentype:
            case 0:
                numbits = read_i(15)
                endcursor = cursor + numbits
                subpackets = []
                while cursor < endcursor:
                    subpackets.append(read_packet())
                return subpackets
            case 1:
                numpackets = read_i(11)
                subpackets = [read_packet() for _ in range(numpackets)]
                return subpackets
    packet = read_packet()
    return packet


def read_input(kind):
    with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
        return f.read()


if __name__ == "__main__":
    examples = [
        'D2FE28',
        '38006F45291200',
        'EE00D40C823060',
        '8A004A801A8002F478',
        '620080001611562C8802118E34',
        'C0015000016115A2E0802F182340',
        'A0016C880162017C3686B18A3D4780',
    ]
    for example in examples:
        part_one(parse(example))
    part_one(parse(read_input('input')))

    examples = [
        'C200B40A82',
        '04005AC33890',
        '880086C3E88112',
        'CE00C43D881120',
        'D8005AC2A8F0',
        'F600BC2D8F',
        '9C005AC2F8F0',
        '9C0141080250320F1802104A08',
    ]
    for example in examples:
        part_two(parse(example))
    part_two(parse(read_input('input')))
