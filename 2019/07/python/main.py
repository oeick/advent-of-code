from itertools import permutations

from computer import Computer


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        program = [int(n) for n in fp.read().split(',')]
    return solve_part_1(program), solve_part_2(program)


def solve_part_1(program: list[int]) -> int:
    max_output = 0
    for signal_sequence in permutations((0, 1, 2, 3, 4)):
        output = 0
        for signal in signal_sequence:
            comp = Computer(program, inp=[signal, output])
            result = comp.run()
            if result is not None:
                output = result
        if output > max_output:
            max_output = output
    return max_output


def solve_part_2(program: list[int]) -> int:
    max_output = 0
    for signal_sequence in permutations((5, 6, 7, 8, 9)):
        comps = [Computer(program, [s, ]) for s in signal_sequence]
        max_output = calc_feedback_loop(signal_sequence, comps, max_output)
    return max_output


def calc_feedback_loop(signal_sequence: list[int],
                       computers: list[Computer],
                       start_output: int) -> int:
    output, result = 0, 0
    max_output = start_output
    while result is not None:
        for i, signal in enumerate(signal_sequence):
            computers[i].inp.append(output)
            result = computers[i].run()
            if result is not None:
                output = result
        if output > max_output:
            max_output = output
    return max_output


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
