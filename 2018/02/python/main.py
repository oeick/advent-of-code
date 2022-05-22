from itertools import product
from functools import reduce
from collections import Counter


def count_double_and_triple_chars(strings: list[str]) -> (int, int):
    return reduce(lambda a, b: (a[0] + (2 in b),
                                a[1] + (3 in b)),
                  [Counter(s).values() for s in strings],
                  (0, 0))


def solve_part_2(strings: list[str]) -> str:
    for string_1, string_2 in product(strings, strings):
        mutual = [c1 for c1, c2 in zip(string_1, string_2) if c1 == c2]
        if len(mutual) == len(string_1) - 1:
            return ''.join(mutual)


def solve_part_1(box_ids: list[str]) -> int:
    doublets, triplets = count_double_and_triple_chars(box_ids)
    return doublets * triplets


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        box_ids = fp.read().splitlines()
    return solve_part_1(box_ids), solve_part_2(box_ids)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
