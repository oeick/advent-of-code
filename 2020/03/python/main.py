import math


with open('../input.txt', 'r') as input_file:
    input_lines = [line.strip() for line in input_file.readlines()]


def count_trees(lines, right, down):
    return len([line for i, line in enumerate(lines[::down])
                if line[i * right % len(line)] == '#'])


def solve(lines, slopes):
    return math.prod(count_trees(lines, r, d) for r, d in slopes)


print(solve(input_lines, [(3, 1)]))
print(solve(input_lines, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
