from functools import lru_cache


@lru_cache
def populate(start_value: int, days: int) -> int:
    next_generation = ((days - start_value - 1) // 7) + 1
    return next_generation + sum(
        [populate(8, days - start_value - i * 7 - 1)
         for i in range((days - start_value) // 7)])


def solve(start_values: list[int], days: int) -> int:
    return len(start_values) + sum(populate(s, days) for s in start_values)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        timers = [int(n) for n in fp.read().split(',')]
    return solve(timers, 80), solve(timers, 256)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
