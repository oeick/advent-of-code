def solve(lines: list[str]) -> (int, int):
    return len(lines), len(lines[0])


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    return solve(lines)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
