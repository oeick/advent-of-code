from math import prod
from itertools import combinations


def solve(values: list[int], num_of_groups: int) -> int:
    weight = sum(values) // num_of_groups
    candidates = []
    size = 2
    while not candidates:
        for group in combinations(values, size):
            if sum(group) == weight:
                candidates.append(group)
        size += 1
    return min(prod(c) for c in candidates)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        values = [int(v) for v in fp.read().splitlines()]
    return (solve(values, 3),
            solve(values, 4))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
