import re
from typing import Optional

ABBA_PATTERN: re.Pattern = re.compile(r'(\w)(\w)\2\1')


def search_abba(line: str) -> Optional[str]:
    match = ABBA_PATTERN.search(line)
    return match[0] if match and match[0][0] != match[0][1] else None


def is_valid(line: str) -> bool:
    tokens = re.split(r'[\[|\]]', line)
    abba_outside_brackets = any(search_abba(t) for t in tokens[::2])
    abba_inside_brackets = any(search_abba(t) for t in tokens[1::2])
    return abba_outside_brackets and not abba_inside_brackets


def solve(lines: list[str]) -> int:
    valid_lines = [is_valid(line) for line in lines]
    return valid_lines.count(True)


def main(filename: str) -> int:
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    return solve(lines)


if __name__ == '__main__':
    solution = main('../input.txt')
    print(solution)
