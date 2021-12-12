from typing import NamedTuple

#      --0--
#     |     |
#     1     2
#     |     |
#      --3--
#     |     |
#     4     5
#     |     |
#      --6--


class Wiring(NamedTuple):
    wires: list[str]
    output: list[str]


def solve_part_1(wiring: list[Wiring]) -> int:
    return sum(1 for w in wiring for s in w.output if len(s) in [2, 3, 4, 7])


def remove(target_values: str,
           segments: dict[int, str],
           target_keys: set[int]) -> dict[int, str]:
    new_segments = {k: v for k, v in segments.items() if k not in target_keys}
    new_segments |= {k: ''.join([v for v in segments[k]
                                 if v not in target_values])
                     for k in target_keys}
    return new_segments


def keep(target_values: str,
         segments: dict[int, str],
         target_key: int) -> str:
    return ''.join([v for v in segments[target_key] if v in target_values])


def fixate(segments: dict[int, str],
           wire: str,
           indexes: set) -> dict[int, str]:
    for i in indexes:
        segments[i] = keep(wire, segments, i)
    return remove(wire, segments, set(range(7)) - indexes)


def deduct(segments: dict[int, str],
           wire: str,
           signature: list[int],
           hits: list[int]):
    wires_target = set(''.join(segments[s] for s in signature))
    wire_diff = set(wire) - set(wires_target)
    if len(wire_diff) == 1:
        segments[hits[0]] = wire_diff.pop()
        segments[hits[1]] = [v for v in segments[hits[1]]
                             if v not in segments[hits[0]]].pop()


def decode_wiring(wires: list[str]) -> dict[int, str]:
    segments = {n: 'abcdefg' for n in range(7)}
    while any(len(v) > 1 for v in segments.values()):
        for wire in wires:
            if 2 <= len(wire) <= 4:
                segments = fixate(segments, wire, {
                    2: {2, 5}, 3: {0, 2, 5}, 4: {1, 2, 3, 5}}[len(wire)])
            elif len(wire) == 5 and len(segments[0]) == 1 and len(segments[6]) == 1:
                if len(segments[1]) == 2:
                    deduct(segments, wire, [0, 2, 5, 6], [3, 1])
                elif len(segments[1]) == 1 and len(segments[2]) == 2:
                    deduct(segments, wire, [0, 1, 3, 6], [5, 2])
            elif len(wire) == 6:
                if len(segments[0]) == 1 and len(segments[1]) == 2:
                    deduct(segments, wire, [0, 1, 2], [6, 4])
    return segments


def generate_digit_mapping(segments: dict[int, str]) -> dict[frozenset, int]:
    def map_to(*indexes):
        return frozenset({segments[i] for i in indexes})
    return {
        map_to(0, 1, 2, 4, 5, 6): 0,
        map_to(2, 5): 1,
        map_to(0, 2, 3, 4, 6): 2,
        map_to(0, 2, 3, 5, 6): 3,
        map_to(1, 2, 3, 5): 4,
        map_to(0, 1, 3, 5, 6): 5,
        map_to(0, 1, 3, 4, 5, 6): 6,
        map_to(0, 2, 5): 7,
        map_to(0, 1, 2, 3, 4, 5, 6): 8,
        map_to(0, 1, 2, 3, 5, 6): 9,
    }


def read_digits(output: list[str], segments: dict[int, str]) -> int:
    reading = generate_digit_mapping(segments)
    return int(''.join(str(reading[frozenset(op)]) for op in output))


def solve_part_2(wiring: list[Wiring]) -> int:
    return sum(read_digits(output, decode_wiring(wires))
               for wires, output in wiring)


def parse(line: str) -> Wiring:
    token = [x for x in line.split('|')]
    return Wiring(token[0].split(), token[1].split())


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        signals = [parse(line) for line in fp.read().splitlines()]
    return solve_part_1(signals), solve_part_2(signals)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
