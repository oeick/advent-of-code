import re
from typing import NamedTuple

REPLACEMENT_PATTERN = re.compile(r'(.*) => (.*)\n')


class Replacement(NamedTuple):
    old: str
    new: str

    def apply(self, molecule: str, position: int) -> str:
        return molecule[:position] + \
               self.new + \
               molecule[position + len(self.old):]


def parse_lines(lines: list) -> (list, str):
    replacements = [Replacement(*REPLACEMENT_PATTERN.match(r).groups())
                    for r in lines[:-2]]
    return replacements, lines[-1]


def find_replacement_possibilities(
        replacement: Replacement, medicine: str) -> list:
    return [replacement.apply(medicine, p)
            for p in find_replacement_positions(replacement, medicine)]


def find_replacement_positions(replacement: Replacement, molecule: str) -> list:
    return [f.span()[0] for f in re.finditer(replacement.old, molecule)]


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
