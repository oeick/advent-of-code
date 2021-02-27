def solve_part_1(instructions: str) -> int:
    return instructions.count('(') - instructions.count(')')


def solve_part_2(instructions: str) -> int:
    floor = 0
    for n, c in enumerate(instructions):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return n + 1


def main(filename: str) -> (int, int):
    with open(filename, 'r') as input_file:
        instructions = input_file.read()
    return (solve_part_1(instructions),
            solve_part_2(instructions))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
