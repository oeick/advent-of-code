import math


def count_trees(lines: list[str], right: int, down: int) -> int:
    return len([line for i, line in enumerate(lines[::down])
                if line[i * right % len(line)] == '#'])


def solve(lines: list[str], slopes: list[tuple[int, int]]) -> int:
    return math.prod(count_trees(lines, r, d) for r, d in slopes)


def main(filename: str) -> (str, str):
    with open(filename, 'r') as input_file:
        input_lines = input_file.read().splitlines()
    solution1 = solve(input_lines, [(3, 1)])
    solution2 = solve(input_lines, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
    return (str(solution1),
            str(solution2))


if __name__ == '__main__':
    solutions = main('../input.txt')
    print(solutions[0])
    print(solutions[1])
