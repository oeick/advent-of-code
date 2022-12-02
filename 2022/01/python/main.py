def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve(lines)


def solve(lines: list[str]) -> tuple[int, int]:
    calories = [0]
    for line in lines:
        if line:
            calories[-1] += int(line)
        else:
            calories.append(0)
    sorted_cal = sorted(calories)
    return sorted_cal[-1], sum(sorted_cal[-3:])


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
