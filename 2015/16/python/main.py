import re

NUMBER_PATTERN = re.compile(r'(\d+):')
COMPOUND_PATTERN = re.compile(r'\w+: \d+')


MFCSAM_OUTPUT = [
    'children: 3',
    'cats: 7',
    'samoyeds: 2',
    'pomeranians: 3',
    'akitas: 0',
    'vizslas: 0',
    'goldfish: 5',
    'trees: 3',
    'cars: 2',
    'perfumes: 1']


def solve_part_1(lines: list[str]) -> int:
    for line in lines:
        number = NUMBER_PATTERN.search(line).group(1)
        compounds = COMPOUND_PATTERN.findall(line)
        if all(c in MFCSAM_OUTPUT for c in compounds):
            return int(number)


def solve(lines: list[str]) -> (int, int):
    return solve_part_1(lines), 0


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    return solve(lines)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
