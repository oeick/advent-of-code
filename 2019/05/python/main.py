from __future__ import annotations
from computer import Computer


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        program = [int(n) for n in fp.read().split(',')]
    return (solve(program, initial_input=1),
            solve(program, initial_input=5))


def solve(program: list[int], initial_input: int) -> int:
    computer = Computer(program, initial_input)
    computer.run()
    return computer.out


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
