from typing import Iterator

DOT = tuple[int, int]
INS = tuple[str, int]


def fold_x(dots: list[DOT], x: int) -> set[DOT]:
    return {((2 * x - d[0]), d[1]) if d[0] > x else d for d in dots}


def fold_y(dots: list[DOT], y: int) -> set[DOT]:
    return {(d[0], (2 * y - d[1])) if d[1] > y else d for d in dots}


def fold(dots: list[DOT], instructions: list[INS]) -> list[DOT]:
    folded = dots
    for axis, value in instructions:
        folded = fold_x(folded, value) if axis == 'x' \
            else fold_y(folded, value)
    return folded


def dots_to_strings(dots: list[DOT]) -> list[str]:
    x_max, y_max = max(dots)[0], max(dots, key=lambda d: d[1])[1]
    matrix = [list(['.' for _ in range(x_max + 1)]) for _ in range(y_max + 1)]
    for x, y in dots:
        matrix[y][x] = '#'
    return [''.join(row) for row in matrix]


def solve_part_1(dots: list[DOT], instruction: INS) -> int:
    folded = fold_x(dots, instruction[1]) if instruction[0] == 'x' \
        else fold_y(dots, instruction[1])
    return len(folded)


def solve_part_2(dots: list[DOT], instructions: list[INS]):
    folded = fold(dots, instructions)
    strings = dots_to_strings(folded)
    return '\n'.join(strings)


def parse_dot(lines: list[str]) -> Iterator[DOT]:
    for line in lines:
        if ',' in line:
            dot = line.split(',')
            yield int(dot[0]), int(dot[1])


def parse_instruction(lines: list[str]) -> Iterator[INS]:
    for line in lines:
        if line[:4] == 'fold':
            axis, value = line.split()[2].split('=')
            yield axis, int(value)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    dots = [d for d in parse_dot(lines)]
    instructions = [i for i in parse_instruction(lines)]
    return solve_part_1(dots, instructions[0]), solve_part_2(dots, instructions)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
