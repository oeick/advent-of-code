import re

PAIR = tuple[int, int]
PAIRS = list[tuple[PAIR, PAIR]]
PATTERN = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')


def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    pairs = parse_pairs(lines)
    return solve(pairs)


def parse_pairs(lines: list[str]) -> PAIRS:
    matches = [PATTERN.match(line).groups() for line in lines]
    ids = [(int(v) for v in m) for m in matches]
    pairs = [((p1a, p1b), (p2a, p2b)) for p1a, p1b, p2a, p2b in ids]
    return pairs


def solve(pairs: PAIRS) -> tuple[int, int]:
    return (
        sum(is_in(p1, p2) or is_in(p2, p1) for p1, p2 in pairs),
        sum(overlaps(p1, p2) or overlaps(p2, p1) for p1, p2 in pairs))


def is_in(p1: PAIR, p2: PAIR) -> bool:
    return p1[0] >= p2[0] and p1[1] <= p2[1]


def overlaps(p1: PAIR, p2: PAIR) -> bool:
    return p2[1] >= p1[0] >= p2[0] or p2[1] >= p1[1] >= p2[0]


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
