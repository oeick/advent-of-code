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


def solve_part_1(sues: dict[str, list]) -> int:
    for number, compounds in sues.items():
        if all(c in MFCSAM_OUTPUT for c in compounds):
            return int(number)


def solve_part_2(sues: dict[str, list]) -> int:
    mfcsam_dict = {c.split()[0]: int(c.split()[1]) for c in MFCSAM_OUTPUT}
    for number, compounds in sues.items():
        valid = True
        for compound in compounds:
            kind, amount_str = compound.split()
            amount = int(amount_str)
            if kind in ['cats:', 'trees:']:
                if amount <= mfcsam_dict[kind]:
                    valid = False
                    continue
            elif kind in ['pomeranians:', 'goldfish:']:
                if amount >= mfcsam_dict[kind]:
                    valid = False
                    continue
            else:
                if amount != mfcsam_dict[kind]:
                    valid = False
                    continue
        if valid:
            return int(number)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    sues = {
        NUMBER_PATTERN.search(line).group(1): COMPOUND_PATTERN.findall(line)
        for line in lines}
    return solve_part_1(sues), solve_part_2(sues)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
