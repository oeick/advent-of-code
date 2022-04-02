from typing import Callable, Iterable


def solve(instructions: Iterable[int], modifier: Callable) -> int:
    offsets = list(instructions)
    position, steps = 0, 0
    while 0 <= position < len(offsets):
        steps += 1
        new_position = position + offsets[position]
        offsets[position] += modifier(offsets[position])
        position = new_position
    return steps


def solve_part_1(instructions: Iterable[int]) -> int:
    return solve(instructions, lambda _: 1)


def solve_part_2(instructions: Iterable[int]) -> int:
    return solve(instructions, lambda o: 1 if o < 3 else -1)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        instructions = [int(i) for i in fp.read().splitlines()]
    return solve_part_1(instructions), solve_part_2(instructions)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
