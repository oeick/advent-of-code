def solve(pos: list[int]) -> (int, int):
    cheap = min(get_cheap_fuel(pos, x) for x in range(max(pos)))
    expensive = min(get_expensive_fuel(pos, x) for x in range(max(pos)))
    return cheap, expensive


def get_cheap_fuel(positions: list[int], x: int) -> int:
    return sum(abs(p - x) for p in positions)


def get_expensive_fuel(positions: list[int], x: int) -> int:
    return sum((abs(p - x) * (abs(p - x) + 1)) // 2 for p in positions)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        positions = [int(n) for n in fp.read().split(',')]
    return solve(positions)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
