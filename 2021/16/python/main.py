import operator
from functools import reduce
from typing import Iterator


def hex2bin(hex_string: str) -> str:
    bin_string = bin(int(hex_string, base=16))[2:]
    leading_zeros = '0' * (len(hex_string) * 4 - len(bin_string))
    return leading_zeros + bin_string


def literal_nibbles(bits: str) -> Iterator[str]:
    i = 0
    yield bits[1:5]
    while bits[i] == '1':
        i += 5
        yield bits[i + 1:i + 5]


def parse_literal(load: str) -> (int, int):
    nibbles = [n for n in literal_nibbles(load)]
    return len(nibbles) * 5, int(''.join(nibbles), 2)


def parse_operator_subs_by_length(load: str) -> (int, list):
    length = int(load[1:16], 2)
    _, sub_packets = parse_packets(load[16:16 + length])
    return 16 + length, sub_packets


def parse_operator_subs_by_number(load: str) -> (int, list):
    number = int(load[1:12], 2)
    i = 12
    packets = []
    for n in range(number):
        used_bits, packet = parse_packet(load[i:])
        i += used_bits
        packets.append(packet)
    return i, packets


def parse_operator(load: str) -> (int, list):
    length_type_id = load[0]
    if length_type_id == '0':
        return parse_operator_subs_by_length(load)
    else:
        return parse_operator_subs_by_number(load)


def parse_packet(load: str) -> (int, dict):
    if len(load) < 11:
        return 0, None
    packet = {'version': int(load[:3], 2), 'type_id': int(load[3:6], 2)}
    if packet['type_id'] == 4:
        used_bits, literal = parse_literal(load[6:])
        return used_bits + 6, packet | {'literal': literal}
    else:
        used_bits, sub_packets = parse_operator(load[6:])
        return used_bits + 6, packet | {'sub-packets': sub_packets}


def parse_packets(load: str) -> (int, list):
    packets = []
    i, packet = parse_packet(load)
    if packet:
        packets.append(packet)
    while packet:
        used_bits, packet = parse_packet(load[i:])
        if packet:
            packets.append(packet)
            i += used_bits
    return i, packets


def sum_versions(packet: dict) -> int:
    versions = packet['version']
    if packet['type_id'] != 4:
        versions += sum(sum_versions(s) for s in packet['sub-packets'])
    return versions


def apply_operator(packets: list[dict], op) -> int:
    return int(reduce(op, [calculate_value(p) for p in packets]))


def calculate_value(packet: dict) -> int:
    if packet['type_id'] == 4:
        return packet['literal']
    else:
        return apply_operator(packet['sub-packets'], {
            0: operator.add,
            1: operator.mul,
            2: min,
            3: max,
            5: operator.gt,
            6: operator.lt,
            7: operator.eq
        }[packet['type_id']])


def solve_part_1(hex_string: str) -> int:
    bin_string = hex2bin(hex_string)
    _, packet = parse_packet(bin_string)
    return sum_versions(packet)


def solve_part_2(hex_string: str) -> int:
    bin_string = hex2bin(hex_string)
    _, packet = parse_packet(bin_string)
    return calculate_value(packet)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        content = fp.read()
    return solve_part_1(content), solve_part_2(content)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
