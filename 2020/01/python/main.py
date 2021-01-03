import itertools
import math


def solve(numbers: list[int], num_of_entries: int) -> int:
    combis = itertools.combinations(numbers, num_of_entries)
    values = next(combis)
    while sum(values) != 2020:
        values = next(combis)
    return math.prod(values)


def main(filename: str) -> (str, str):
    with open(filename, 'r') as input_file:
        input_numbers = [int(line.strip()) for line in input_file.readlines()]
    return (str(solve(input_numbers, 2)),
            str(solve(input_numbers, 3)))


if __name__ == '__main__':
    solutions = main('../input.txt')
    print(solutions[0])
    print(solutions[1])
