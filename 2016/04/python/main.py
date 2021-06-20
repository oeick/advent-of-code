import re
import string
from collections import Counter


def get_five_most_common(name: str) -> list[(str, int)]:
    count_dict = Counter([c for c in name if c.isalpha()])
    count_tuple = [(c, count_dict[c]) for c in count_dict]
    return sorted(count_tuple, key=lambda x: (-x[1], x[0]))[:5]


def validate(name: str, checksum: str) -> bool:
    return ''.join([c[0] for c in get_five_most_common(name)]) == checksum


def rotate(char: str, n: int) -> str:
    """ Rotates char by n times through the alphabet. """
    return chr(
        ord('a') + (ord(char) - ord('a') + n) % len(string.ascii_lowercase))


def decipher(name: str, sector_id: int) -> str:
    return ''.join(rotate(c, sector_id) if c.isalpha() else ' ' for c in name)


def get_valid_rooms(lines: list[str]) -> (str, int):
    pattern = re.compile(r'(.+)-(\d+)\[(.+)]')
    for line in lines:
        name, sector, checksum = pattern.match(line).groups()
        if validate(name, checksum):
            yield name, int(sector)


def solve(lines: list[str], search: str) -> (int, int):
    id_sum = sum(s for _, s in get_valid_rooms(lines))
    storage = next(s for n, s in get_valid_rooms(lines)
                   if decipher(n, s) == search)
    return id_sum, storage


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve(lines, "northpole object storage")


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
