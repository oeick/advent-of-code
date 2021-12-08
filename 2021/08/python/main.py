from typing import NamedTuple


class Wiring(NamedTuple):
    wires: list[str]
    segments: list[str]


def solve_part_1(wiring: list[Wiring]) -> int:
    return sum(1 for w in wiring for s in w.segments if len(s) in [2, 3, 4, 7])


def parse(line: str) -> Wiring:
    token = [x for x in line.split('|')]
    return Wiring(token[0].split(), token[1].split())


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        signals = [parse(line) for line in fp.read().splitlines()]
    return solve_part_1(signals), 0


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
