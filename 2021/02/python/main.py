def solve_part_1(commands: list[tuple[str, int]]) -> int:
    horizontal = sum(v for d, v in commands if d == 'forward')
    depth = sum(v if d == 'down' else -v for d, v in commands if d != 'forward')
    return horizontal * depth


def solve_part_2(commands: list[tuple[str, int]]) -> int:
    aim, horizontal, depth = 0, 0, 0
    for direction, value in commands:
        if direction == 'forward':
            horizontal += value
            depth += aim * value
        else:
            aim += value if direction == 'down' else -value
    return horizontal * depth


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        tokens = [line.split() for line in fp.read().splitlines()]
    commands = [(d, int(v)) for d, v in tokens]
    return solve_part_1(commands), solve_part_2(commands)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
