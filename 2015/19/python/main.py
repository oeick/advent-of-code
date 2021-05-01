import re

REPLACEMENT_PATTERN = re.compile(r'(.*) => (.*)\n')


def parse_lines(lines: list) -> (list, str):
    replacements = [REPLACEMENT_PATTERN.match(r).groups() for r in lines[:-2]]
    return replacements, lines[-1]


def find_replacement_possibilities(replacement: tuple, medicine: str) -> list:
    possibilities = []
    index, relative_index = 0, 0
    while relative_index > -1:
        relative_index = medicine[index:].find(replacement[0])
        if relative_index > -1:
            index += relative_index
            possibilities.append(
                medicine[:index] +
                replacement[1] +
                medicine[index + len(replacement[0]):])
            index += len(replacement[0])
    return possibilities


def find_distinct_molecules(replacements: list, medicine: str) -> set:
    molecules = set()
    for replacement in replacements:
        molecules |= set(find_replacement_possibilities(replacement, medicine))
    return molecules


def solve_part_1(replacements: list, medicine: str) -> int:
    return len(find_distinct_molecules(replacements, medicine))


def solve_part_2(replacements: list, medicine: str) -> int:
    return 0


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    replacements, medicine = parse_lines(lines)
    return (solve_part_1(replacements, medicine),
            solve_part_2(replacements, medicine))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
