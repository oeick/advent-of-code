import re
from itertools import product
from typing import Iterable

PATTERN = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
SQUARES = set[tuple[int, int]]


def main(filename: str) -> (int, str):
    with open(filename, 'r') as fp:
        claims = parse_claims(fp)
    return solve(claims)


def solve(claims: dict[str, SQUARES]) -> (int, str):
    overlaps = find_overlaps(claims)
    intact_claim = next(claim_id for claim_id, claim in claims.items()
                        if claim.isdisjoint(overlaps))
    return len(overlaps), intact_claim


def parse_claims(lines: Iterable[str]) -> dict[str, SQUARES]:
    claims = dict()
    for line in lines:
        claim_id, claim = parse_claim(line)
        claims[claim_id] = claim
    return claims


def parse_claim(line: str) -> (str, SQUARES):
    match = PATTERN.search(line)
    claim_id = match[1]
    x1, y1 = int(match[2]), int(match[3])
    x2, y2 = x1 + int(match[4]), y1 + int(match[5])
    return claim_id, set(product(range(x1, x2), range(y1, y2)))


def find_overlaps(claims: dict[str, SQUARES]) -> SQUARES:
    claimed_squares, overlapping = set(), set()
    for claim_id, claim in claims.items():
        overlap = claim.intersection(claimed_squares)
        overlapping |= overlap
        claimed_squares |= claim
    return overlapping


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
