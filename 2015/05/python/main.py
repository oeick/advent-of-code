import re

VOWEL_PATTERN = re.compile(r"[aeiou]")
DOUBLE_PATTERN = re.compile(r".*(.)\1")

ABA_PATTERN = re.compile(r".*(.).\1")
PAIR_PATTERN = re.compile(r".*(..).*\1")


def is_nice1(line: str) -> bool:
    matches_3vowels = re.findall(VOWEL_PATTERN, line)
    matches_doubles = re.match(DOUBLE_PATTERN, line)
    return \
        len(matches_3vowels) >= 3 \
        and matches_doubles \
        and 'ab' not in line \
        and 'cd' not in line \
        and 'pq' not in line \
        and 'xy' not in line


def is_nice2(line: str) -> bool:
    matches_aba = re.match(ABA_PATTERN, line)
    matches_pair = re.match(PAIR_PATTERN, line)
    return bool(matches_aba and matches_pair)


def get_nice_lines1(lines: list[str]) -> list[str]:
    return [line for line in lines if is_nice1(line)]


def get_nice_lines2(lines: list[str]) -> list[str]:
    return [line for line in lines if is_nice2(line)]


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return (len(get_nice_lines1(lines)),
            len(get_nice_lines2(lines)))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
