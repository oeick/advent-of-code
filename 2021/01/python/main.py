def solve(lines: list[str]) -> (int, int):
    numbers = [int(line) for line in lines]
    solution1 = len([i for i in range(1, len(numbers))
                     if numbers[i] > numbers[i-1]])
    solution2 = len([i for i in range(3, len(numbers))
                     if sum(numbers[i-2:i+1]) > sum(numbers[i-3:i])])
    return solution1, solution2


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve(lines)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
