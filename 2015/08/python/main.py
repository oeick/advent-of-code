def solve_part_1(lines: list[str]) -> int:
    return sum(len(line) - len(eval(line)) for line in lines)


def solve_part_2(lines: list[str]) -> int:
    return sum(2 + line.count('"') + line.count('\\') for line in lines)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return (solve_part_1(lines),
            solve_part_2(lines))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
