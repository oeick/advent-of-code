from operator import add, mul
from itertools import product
from typing import Final, Callable

OPERATIONS: Final[dict[int, Callable[[int, int], int]]] = {1: add, 2: mul}


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        program = [int(n) for n in fp.read().split(',')]
    return solve_part_1(program), solve_part_2(program, target=19690720)


def solve_part_1(program: list[int]) -> int:
    return run_program(program, noun=12, verb=2)[0]


def solve_part_2(program: list[int], target: int) -> int:
    for noun, verb in product(range(100), range(100)):
        output = run_program(program, noun, verb)[0]
        if output == target:
            break
    else:
        raise ValueError(f'No noun and verb found to reach {target}')
    return noun * 100 + verb


def run_program(program: list[int], noun: int, verb: int) -> list[int]:
    numbers = list(program)
    numbers[1], numbers[2] = noun, verb
    return execute_opcodes(numbers)


def execute_opcodes(program: list[int]) -> list[int]:
    numbers = list(program)
    for i in range(0, len(numbers), 4):
        if (opcode := numbers[i]) == 99:
            break
        param1, param2, target = numbers[i+1:i+4]
        numbers[target] = OPERATIONS[opcode](numbers[param1], numbers[param2])
    return numbers


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
