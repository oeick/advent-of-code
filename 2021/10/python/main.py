import re
from typing import Optional

PATTERN = re.compile(r'[\[({<][])}>]')
PAIRS = ['[]', '{}', '()', '<>']


def get_corrupted_char(line: str) -> Optional[str]:
    remaining_line = line
    while match := PATTERN.findall(remaining_line):
        if match[0] not in PAIRS:
            return match[0][1]
        remaining_line = remaining_line.replace(match[0], '', 1)


def solve_part_1(lines: list[str]) -> int:
    chars = [get_corrupted_char(line) for line in lines]
    score = sum({')': 3, ']': 57, '}': 1197, '>': 25137}[c]
                for c in chars if c)
    return score


def inverse(char: str) -> str:
    return {o: c for o, c in PAIRS}[char]


def complete(line: str) -> str:
    remaining_line = line
    while match := PATTERN.findall(remaining_line):
        remaining_line = remaining_line.replace(match[0], '', 1)
    return ''.join([inverse(c) for c in remaining_line[::-1]])


def calc_score(chars: str) -> int:
    score = 0
    for char in chars:
        score *= 5
        score += {')': 1, ']': 2, '}': 3, '>': 4}[char]
    return score


def solve_part_2(lines: list[str]) -> int:
    incomplete = [line for line in lines if not get_corrupted_char(line)]
    added_chars = [complete(line) for line in incomplete]
    scores = [calc_score(c) for c in added_chars]
    return sorted(scores)[len(scores) // 2]


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve_part_1(lines), solve_part_2(lines)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
