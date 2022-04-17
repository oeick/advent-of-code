from itertools import accumulate, cycle


def solve_part_1(changes: list[int]) -> int:
    return list(accumulate(changes))[-1]


def solve_part_2(changes: list[int]) -> int:
    frequencies = {0}
    frequency_generator = accumulate(cycle(changes))
    while (frequency := next(frequency_generator)) not in frequencies:
        frequencies.add(frequency)
    return frequency


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        changes = [int(v) for v in fp.read().splitlines()]
    return solve_part_1(changes), solve_part_2(changes)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
