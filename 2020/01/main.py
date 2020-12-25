import itertools
import math

with open('input.txt', 'r') as input_file:
    input_numbers = [int(line.strip()) for line in input_file.readlines()]


def solve(numbers, num_of_entries):
    combis = itertools.combinations(numbers, num_of_entries)
    values = next(combis)
    while sum(values) != 2020:
        values = next(combis)
    return math.prod(values)


print(solve(input_numbers, 2))
print(solve(input_numbers, 3))
